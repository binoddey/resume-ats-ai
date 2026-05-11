import re

# ======================================
# NORMALIZED SKILL DATABASE
# ======================================

SKILLS_DB = {

    # Frontend
    "html": ["html"],

    "css": ["css"],

    "javascript": [
        "javascript",
        "js"
    ],

    "react": [
        "react",
        "reactjs",
        "react.js"
    ],

    "redux": ["redux"],

    "angular": [
        "angular",
        "angularjs",
        "angular 7",
        "angular 8",
        "angular 9",
        "angular 10",
        "angular 11",
        "angular 12",
        "angular 13",
        "angular 14",
        "angular 15",
        "angular 16",
        "angular 17"
    ],

    "bootstrap": ["bootstrap"],

    "jquery": [
        "jquery",
        "j query"
    ],

    "tailwind": [
        "tailwind",
        "tailwindcss"
    ],

    # Backend
    "flask": ["flask"],

    "django": ["django"],

    "nodejs": [
        "nodejs",
        "node.js"
    ],

    # Database
    "mysql": ["mysql"],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "mongodb": ["mongodb"],

    # DevOps
    "docker": ["docker"],

    "aws": ["aws"],

    "vercel": ["vercel"],

    # APIs
    "rest api": [
        "rest api",
        "restful api",
        "rest apis"
    ],

    # Tools
    "git": ["git"],

    "github": ["github"]
}

# ======================================
# SKILL EXTRACTION
# ======================================

def extract_skills(text):

    text = text.lower()

    detected_skills = set()

    for normalized_skill, variants in SKILLS_DB.items():

        for variant in variants:

            pattern = (
                r'\b'
                + re.escape(variant.lower())
                + r'\b'
            )

            if re.search(pattern, text):

                detected_skills.add(
                    normalized_skill
                )

                break

    return list(detected_skills)