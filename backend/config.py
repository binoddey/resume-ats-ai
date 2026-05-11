import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

class Config:

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY"
    )

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads"
    )

    RESUME_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "resumes"
    )

    GENERATED_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "generated"
    )

    TEMP_FOLDER = os.path.join(
        UPLOAD_FOLDER,
        "temp"
    )

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx",
        "txt"
    }