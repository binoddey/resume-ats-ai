from openai import OpenAI

from config import Config

# =====================================
# OPENROUTER CLIENT
# =====================================

client = OpenAI(

    api_key=Config.OPENROUTER_API_KEY,

    base_url="https://openrouter.ai/api/v1"
)

# =====================================
# AI FEEDBACK
# =====================================

def generate_ai_feedback(

    ats_score,

    matched_skills,

    missing_skills,

    suggestions,

    readability_score,

    action_verb_score
):

    prompt = f"""

    You are an expert ATS resume reviewer.

    Analyze this resume evaluation.

    ATS Score:
    {ats_score}

    Matched Skills:
    {matched_skills}

    Missing Skills:
    {missing_skills}

    Existing Suggestions:
    {suggestions}

    Readability Score:
    {readability_score}

    Action Verb Score:
    {action_verb_score}

    Give:

    1. ATS optimization advice
    2. Resume improvement suggestions
    3. Better keyword recommendations
    4. Better recruiter appeal suggestions
    5. Stronger bullet point wording ideas

    Keep response:
    - concise
    - actionable
    - professional
    - bullet-point based
    """

    try:

        response = client.chat.completions.create(

            model="openrouter/free",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7
        )

        return (

            response
            .choices[0]
            .message.content
        )

    except Exception as e:

        return f"AI feedback failed: {str(e)}"