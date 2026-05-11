import re

# ======================================
# WEAK PHRASES
# ======================================

WEAK_PHRASES = {

    "worked on": "developed",

    "helped": "assisted",

    "responsible for": "managed",

    "did": "executed",

    "made": "built",

    "handled": "coordinated",

    "used": "implemented",

    "participated in": "contributed to"
}

# ======================================
# STRONG ACTION VERBS
# ======================================

STRONG_VERBS = [

    "developed",
    "engineered",
    "optimized",
    "implemented",
    "designed",
    "created",
    "built",
    "managed",
    "led",
    "automated",
    "improved",
    "architected",
    "deployed"
]

# ======================================
# CHECK ACTION VERBS
# ======================================

def analyze_action_verbs(text):

    lower_text = text.lower()

    weak_matches = []

    suggestions = []

    # ----------------------------------
    # Detect Weak Phrases
    # ----------------------------------

    for weak, strong in WEAK_PHRASES.items():

        pattern = (
            r'\\b'
            + re.escape(weak)
            + r'\\b'
        )

        if re.search(pattern, lower_text):

            weak_matches.append(weak)

            suggestions.append(

                f'Replace \"{weak}\" with stronger verbs like \"{strong}\"'
            )

    # ----------------------------------
    # Count Strong Verbs
    # ----------------------------------

    strong_verb_count = 0

    for verb in STRONG_VERBS:

        pattern = (
            r'\b'
            + re.escape(verb)
            + r'\b'
        )

        matches = re.findall(
            pattern,
            lower_text
        )

        strong_verb_count += len(matches)

    # ----------------------------------
    # Verb Quality Score
    # ----------------------------------

    score = 100

    if len(weak_matches) >= 3:

        score -= 25

    elif len(weak_matches) >= 1:

        score -= 10

    if strong_verb_count < 3:

        score -= 15

        suggestions.append(
            "Use more strong action verbs in bullet points"
        )

    if score < 0:
        score = 0

    # ----------------------------------
    # Result
    # ----------------------------------

    return {

        "action_verb_score":
            score,

        "weak_phrases":
            weak_matches,

        "strong_verb_count":
            strong_verb_count,

        "suggestions":
            suggestions
    }