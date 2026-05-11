import streamlit as st
import requests

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="AI Resume Analyzer",

    page_icon="📄",

    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown(
    """
    <style>

    /* ============================= */
    /* APP BACKGROUND */
    /* ============================= */

    .stApp {

        background:
            linear-gradient(
                135deg,
                #0f172a,
                #111827
            );

        color: white;

        font-family: 'Inter', sans-serif;
    }

    /* ============================= */
    /* HEADINGS */
    /* ============================= */

    h1, h2, h3, h4 {

        color: white;
        font-weight: 700;
    }

    /* ============================= */
    /* METRIC CARDS */
    /* ============================= */

    div[data-testid="metric-container"] {

        background:
            rgba(30, 41, 59, 0.7);

        border:
            1px solid rgba(
                255,
                255,
                255,
                0.08
            );

        padding: 20px;

        border-radius: 20px;

        backdrop-filter: blur(10px);

        transition: 0.3s ease;
    }

    div[data-testid="metric-container"]:hover {

        transform: translateY(-3px);

        border:
            1px solid rgba(
                59,
                130,
                246,
                0.5
            );
    }

    /* ============================= */
    /* BUTTON */
    /* ============================= */

    .stButton > button {

        width: 100%;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #3b82f6
            );

        color: white;

        border: none;

        padding: 14px;

        border-radius: 14px;

        font-weight: 600;

        transition: 0.3s ease;
    }

    .stButton > button:hover {

        transform: scale(1.02);

        background:
            linear-gradient(
                135deg,
                #1d4ed8,
                #2563eb
            );
    }

    /* ============================= */
    /* INPUTS */
    /* ============================= */

    textarea,
    input {

        background-color:
            rgba(30, 41, 59, 0.8)
            !important;

        color: white !important;

        border-radius: 14px !important;

        border:
            1px solid rgba(
                255,
                255,
                255,
                0.08
            ) !important;
    }

    /* ============================= */
    /* CONTAINERS */
    /* ============================= */

    .block-container {

        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ============================= */
    /* ALERTS */
    /* ============================= */

    div[data-baseweb="notification"] {

        border-radius: 14px;
    }

    /* ============================= */
    /* SIDEBAR */
    /* ============================= */

    section[data-testid="stSidebar"] {

        background-color: #111827;
    }

    /* ============================= */
    /* SCROLLBAR */
    /* ============================= */

    ::-webkit-scrollbar {

        width: 10px;
    }

    ::-webkit-scrollbar-thumb {

        background: #334155;

        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================
# HEADER
# =========================================

st.title("📄 AI Resume Analyzer")

st.write(
    """
    Analyze resumes using:

    - ATS scoring
    - JD matching
    - Skill extraction
    - Readability analysis
    - Action verb analysis
    - AI-powered suggestions
    """
)

# =========================================
# LAYOUT
# =========================================

left_col, right_col = st.columns(
    [1, 1.4]
)

# =========================================
# LEFT PANEL
# =========================================

with left_col:

    st.subheader(
        "Upload Resume"
    )

    uploaded_file = st.file_uploader(

        "Upload Resume",

        type=["pdf", "docx"]
    )

    job_description = st.text_area(

        "Job Description",

        height=300,

        placeholder=
        "Paste job description here..."
    )

    analyze_button = st.button(

        "Analyze Resume",

        use_container_width=True
    )

# =========================================
# RIGHT PANEL
# =========================================

with right_col:

    st.subheader(
        "ATS Dashboard"
    )

    if analyze_button:

        if uploaded_file is None:

            st.error(
                "Please upload a resume."
            )

        else:

            with st.spinner(
                "Analyzing Resume..."
            ):

                try:

                    # ====================
                    # API REQUEST
                    # ====================

                    files = {

                        "resume": (

                            uploaded_file.name,

                            uploaded_file,

                            uploaded_file.type
                        )
                    }

                    data = {

                        "job_description":
                            job_description
                    }

                    response = requests.post(

                        "http://127.0.0.1:5000/analyze",

                        files=files,

                        data=data
                    )

                    result = response.json()

                    # ====================
                    # ERROR CHECK
                    # ====================

                    if not result.get(
                        "success"
                    ):

                        st.error(

                            result.get(
                                "error",
                                "Analysis failed"
                            )
                        )

                    else:

                        # ====================
                        # METRIC CARDS
                        # ====================

                        col1, col2 = st.columns(2)

                        col3, col4 = st.columns(2)

                        with col1:

                            st.metric(

                                "ATS Score",

                                result[
                                    "ats_score"
                                ]
                            )

                        with col2:

                            st.metric(

                                "JD Match Score",

                                f"{result['jd_match_score']}%"
                            )

                        with col3:

                            st.metric(

                                "Readability",

                                result[
                                    "readability_analysis"
                                ][
                                    "readability_score"
                                ]
                            )

                        with col4:

                            st.metric(

                                "Action Verbs",

                                result[
                                    "action_verb_analysis"
                                ][
                                    "action_verb_score"
                                ]
                            )

                        st.divider()

                        # ====================
                        # DETECTED SKILLS
                        # ====================

                        st.subheader(
                            "Detected Skills"
                        )

                        st.success(

                            ", ".join(

                                result[
                                    "skills_detected"
                                ]
                            )
                        )

                        # ====================
                        # MATCHED SKILLS
                        # ====================

                        st.subheader(
                            "Matched Skills"
                        )

                        st.success(

                            ", ".join(

                                result[
                                    "matched_skills"
                                ]
                            )
                        )

                        # ====================
                        # MISSING SKILLS
                        # ====================

                        st.subheader(
                            "Missing Skills"
                        )

                        st.error(

                            ", ".join(

                                result[
                                    "missing_skills"
                                ]
                            )
                        )

                        st.divider()

                        # ====================
                        # SUGGESTIONS
                        # ====================

                        st.subheader(
                            "Suggestions"
                        )

                        for suggestion in result[
                            "suggestions"
                        ]:

                            st.warning(
                                suggestion
                            )

                        st.divider()

                        # ====================
                        # CATEGORY BREAKDOWN
                        # ====================

                        st.subheader(
                            "ATS Breakdown"
                        )

                        breakdown = result[
                            "category_breakdown"
                        ]

                        for key, value in breakdown.items():

                            st.info(
                                f"{key.replace('_', ' ').title()}: {value}"
                            )

                        st.divider()

                        # ====================
                        # AI SUGGESTIONS
                        # ====================

                        st.subheader(
                            "AI Suggestions"
                        )

                        st.markdown(

                            result[
                                "ai_feedback"
                            ]
                        )

                except Exception as e:

                    st.error(str(e))