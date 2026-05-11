import os

from flask import Flask
from flask import request
from flask import jsonify

from config import Config
from extensions import cors

# from controllers.analyze_controller import (
#     analyze_resume_controller
# )

from parsers.pdf_parser import extract_pdf_text
from parsers.docx_parser import (
    extract_docx_text
)
from services.ats_score_service import calculate_ats_score
from utils.file_handler import (
    allowed_file,
    save_uploaded_file
)


# -----------------------------------
# Import Routes
# -----------------------------------

from routes.analyze_routes import (
    analyze_bp
)

from routes.upload_routes import (
    upload_bp
)

# -----------------------------------

app = Flask(
    __name__,
    static_folder=".",
    static_url_path=""
)

# Load Config
app.config.from_object(Config)

# Initialize Extensions
cors.init_app(app)

# Ensure upload folder exists
os.makedirs(
    app.config["UPLOAD_FOLDER"],
    exist_ok=True
)
os.makedirs(
    app.config["RESUME_FOLDER"],
    exist_ok=True
)

os.makedirs(
    app.config["GENERATED_FOLDER"],
    exist_ok=True
)

os.makedirs(
    app.config["TEMP_FOLDER"],
    exist_ok=True
)

# -----------------------------------
# Register Blueprints
# -----------------------------------

app.register_blueprint(
    analyze_bp
)

app.register_blueprint(
    upload_bp
)


# -----------------------------------
# Helper Functions
# -----------------------------------

# -----------------------------------
# Routes
# -----------------------------------

@app.route("/")
def home():

    return app.send_static_file("index.html")

# -----------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )