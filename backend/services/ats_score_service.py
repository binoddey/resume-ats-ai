from nlp.section_detector import (
    detect_sections
)

# ======================================
# ATS SCORE ENGINE
# ======================================

def calculate_ats_score(

    text,

    jd_result,

    readability_result,

    verb_result
):

    # ==================================
    # INITIALIZATION
    # ==================================

    total_score = 0

    suggestions = []

    detected_sections = detect_sections(
        text
    )

    detected_sections = [
        section.lower()
        for section in detected_sections
    ]

    # ==================================
    # SECTION SCORING (25)
    # ==================================

    required_sections = [

        "education",

        "skills"
    ]

    has_experience = (
        "experience"
        in detected_sections
    )

    has_projects = (
        "projects"
        in detected_sections
    )

    section_score = 0

    # Mandatory sections

    for section in required_sections:

        if section in detected_sections:

            section_score += 10

        else:

            suggestions.append(
                f"Missing required section: {section.title()}"
            )

    # Experience OR Projects

    if has_experience or has_projects:

        section_score += 5

    else:

        suggestions.append(
            "Add Experience or Projects section"
        )

    total_score += section_score

    # ==================================
    # JD MATCH SCORE (30)
    # ==================================

    jd_match_score = min(

        jd_result["match_score"],

        100
    )

    weighted_jd_score = (
        jd_match_score * 0.30
    )

    total_score += weighted_jd_score

    if jd_match_score < 40:

        suggestions.append(
            "Resume poorly matches job description"
        )

    elif jd_match_score < 70:

        suggestions.append(
            "Add more job-relevant skills"
        )

    # ==================================
    # SKILL COVERAGE (15)
    # ==================================

    skill_count = len(
        jd_result["resume_skills"]
    )

    if skill_count >= 10:

        skill_score = 15

    elif skill_count >= 7:

        skill_score = 12

    elif skill_count >= 5:

        skill_score = 8

    else:

        skill_score = 4

        suggestions.append(
            "Add more technical skills"
        )

    total_score += skill_score

    # ==================================
    # READABILITY (10)
    # ==================================

    readability_score = (

        readability_result[
            "readability_score"
        ] * 0.10
    )

    total_score += readability_score

    suggestions.extend(

        readability_result[
            "suggestions"
        ]
    )

    # ==================================
    # ACTION VERBS (10)
    # ==================================

    verb_score = (

        verb_result[
            "action_verb_score"
        ] * 0.10
    )

    total_score += verb_score

    suggestions.extend(

        verb_result[
            "suggestions"
        ]
    )

    # ==================================
    # OPTIONAL SECTIONS (10)
    # ==================================

    optional_sections = [

        "certifications",

        "summary",

        "achievements",

        "leadership"
    ]

    optional_score = 0

    for section in optional_sections:

        if section in detected_sections:

            optional_score += 2.5

    total_score += optional_score

    # ==================================
    # SCORE LIMITS
    # ==================================

    if total_score > 100:
        total_score = 100

    if total_score < 0:
        total_score = 0

    # ==================================
    # REMOVE DUPLICATE SUGGESTIONS
    # ==================================

    suggestions = list(
        set(suggestions)
    )

    # ==================================
    # FINAL RESULT
    # ==================================

    return {

        "score":
            round(total_score, 2),

        "suggestions":
            suggestions,

        "detected_sections":
            detected_sections,

        "category_breakdown": {

            "sections":
                round(section_score, 2),

            "jd_match":
                round(weighted_jd_score, 2),

            "skills":
                round(skill_score, 2),

            "readability":
                round(readability_score, 2),

            "action_verbs":
                round(verb_score, 2),

            "optional_sections":
                round(optional_score, 2)
        }
    }