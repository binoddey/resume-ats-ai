from nlp.skill_extractor import (
    extract_skills
)

def match_resume_to_jd(

    resume_text,

    jd_text
):

    # ==================================
    # EXTRACT SKILLS
    # ==================================

    resume_skills = set(

        extract_skills(
            resume_text
        )
    )

    jd_skills = set(

        extract_skills(
            jd_text
        )
    )

    # ==================================
    # MATCHED SKILLS
    # ==================================

    matched_skills = list(

        resume_skills.intersection(
            jd_skills
        )
    )

    # ==================================
    # MISSING SKILLS
    # ==================================

    missing_skills = list(

        jd_skills - resume_skills
    )
    
    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)

    # ==================================
    # MATCH SCORE
    # ==================================

    if len(jd_skills) == 0:

        match_score = 0

    else:

        match_score = int(

            (
                len(matched_skills)
                / len(jd_skills)
            ) * 100
        )

    # ==================================
    # RESULT
    # ==================================

    return {

        "match_score":
            match_score,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "resume_skills":
            list(resume_skills),

        "jd_skills":
            list(jd_skills)
    }
    
