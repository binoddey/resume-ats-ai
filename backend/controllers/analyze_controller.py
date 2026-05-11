import os

from flask import request
from flask import jsonify
from flask import current_app

from services.ai_feedback_service import (
    generate_ai_feedback
)

from parsers.pdf_parser import (
    extract_pdf_text
)

from parsers.docx_parser import (
    extract_docx_text
)

from nlp.action_verb_checker import (
    analyze_action_verbs
)

from nlp.readability_analyzer import (
    analyze_readability
)

from services.jd_match_service import (
    match_resume_to_jd
)

from services.ats_score_service import (
    calculate_ats_score
)

from nlp.skill_extractor import (
    extract_skills
)

from utils.file_handler import (
    allowed_file,
    save_uploaded_file
)

def analyze_resume_controller():

    # -------------------------------
    # Check File Exists
    # -------------------------------

    if "resume" not in request.files:

        return jsonify({
            "success": False,
            "error": "No file uploaded"
        }), 400

    file = request.files["resume"]

    # -------------------------------
    # Empty Filename
    # -------------------------------

    if file.filename == "":

        return jsonify({
            "success": False,
            "error": "Empty filename"
        }), 400

    # -------------------------------
    # File Validation
    # -------------------------------

    if not allowed_file(
        file.filename,
        current_app.config[
            "ALLOWED_EXTENSIONS"
        ]
    ):

        return jsonify({
            "success": False,
            "error":
                "Only PDF/DOCX allowed"
        }), 400

    # -------------------------------
    # Save File
    # -------------------------------

    saved_file = save_uploaded_file(

        file,

        current_app.config[
            "RESUME_FOLDER"
        ]
    )

    filepath = saved_file["filepath"]

    extension = (
        file.filename
        .rsplit(".", 1)[1]
        .lower()
    )

    try:

        # ---------------------------
        # Parse Resume
        # ---------------------------

        if extension == "pdf":

            text = extract_pdf_text(
                filepath
            )

        elif extension == "docx":

            text = extract_docx_text(
                filepath
            )

        else:

            return jsonify({
                "success": False,
                "error":
                    "Unsupported format"
            }), 400
            
        # ---------------------------
        # JOB DESCRIPTION
        # ---------------------------

        jd_text = request.form.get(
            "job_description",
            ""
        )
        
        # ==================================
        # JD MATCHING
        # ==================================

        jd_result = match_resume_to_jd(

            text,

            jd_text
        )

        # ==================================
        # ACTION VERBS
        # ==================================

        verb_result = analyze_action_verbs(
            text
        )

        # ==================================
        # READABILITY
        # ==================================

        readability_result = analyze_readability(
            text
        )

        # ---------------------------
        # ATS Score
        # ---------------------------

        ats_result = calculate_ats_score(
            text,
            jd_result,
            readability_result,
            verb_result
        )
        
        ai_feedback = generate_ai_feedback(
            ats_result["score"],
            jd_result["matched_skills"],
            jd_result["missing_skills"],
            ats_result["suggestions"],
            readability_result[
                "readability_score"
            ],
            verb_result[
                "action_verb_score"
            ]
        )
        
        # ---------------------------
        # Skill Extraction
        # ---------------------------

        skills = extract_skills(text)
        

        # ---------------------------
        # Final Response
        # ---------------------------

        return jsonify({

            "success": True,

            "filename":
                saved_file["filename"],

            "ats_score":
                ats_result["score"],
                
            "matched_skills":
                jd_result["matched_skills"],

            "missing_skills":
                jd_result["missing_skills"],

            "jd_match_score":
                jd_result["match_score"],

            "suggestions":
                ats_result["suggestions"],

            "skills_detected":
                skills,

            "resume_text":
                text,
            
            "action_verb_analysis":
                verb_result,

            "readability_analysis":
                readability_result,
            
            "category_breakdown":
                ats_result["category_breakdown"],
                
            "ai_feedback":
                ai_feedback,
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500