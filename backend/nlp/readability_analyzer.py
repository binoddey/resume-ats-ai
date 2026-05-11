import re

# ======================================
# READABILITY ANALYZER
# ======================================

def analyze_readability(text):

    # ----------------------------------
    # Word Count
    # ----------------------------------

    words = text.split()

    word_count = len(words)

    # ----------------------------------
    # Sentence Count
    # ----------------------------------

    sentences = re.split(
        r'[.!?]',
        text
    )

    sentences = [
        s for s in sentences
        if s.strip()
    ]

    sentence_count = len(sentences)

    # ----------------------------------
    # Average Sentence Length
    # ----------------------------------

    if sentence_count == 0:

        avg_sentence_length = 0

    else:

        avg_sentence_length = round(

            word_count / sentence_count,

            2
        )

    # ----------------------------------
    # Readability Score
    # ----------------------------------

    score = 100

    suggestions = []

    # Resume too short

    if word_count < 250:

        score -= 25

        suggestions.append(
            "Resume content is too short"
        )

    # Resume too long

    elif word_count > 900:

        score -= 15

        suggestions.append(
            "Resume is too lengthy"
        )

    # Sentences too long

    if avg_sentence_length > 25:

        score -= 15

        suggestions.append(
            "Use shorter and clearer bullet points"
        )

    elif avg_sentence_length < 5:

        score -= 10

        suggestions.append(
            "Descriptions are too brief"
        )

    # ----------------------------------
    # Bullet Point Detection
    # ----------------------------------

    bullet_lines = 0

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if (
            line.startswith("-")
            or line.startswith("•")
            or line.startswith("*")
        ):

            bullet_lines += 1

    if bullet_lines < 3:

        score -= 10

        suggestions.append(
            "Use more bullet points for readability"
        )

    # ----------------------------------
    # Final Limits
    # ----------------------------------

    if score < 0:
        score = 0

    # ----------------------------------
    # Result
    # ----------------------------------

    return {

        "readability_score":
            score,

        "word_count":
            word_count,

        "sentence_count":
            sentence_count,

        "average_sentence_length":
                avg_sentence_length,

        "bullet_points":
            bullet_lines,

        "suggestions":
            suggestions
    }