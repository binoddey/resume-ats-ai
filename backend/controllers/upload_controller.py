from flask import request
from flask import jsonify
from flask import current_app

from utils.file_handler import (
    allowed_file,
    save_uploaded_file
)

def upload_resume_controller():

    if "resume" not in request.files:

        return jsonify({
            "success": False,
            "error": "No file uploaded"
        }), 400

    file = request.files["resume"]

    if file.filename == "":

        return jsonify({
            "success": False,
            "error": "Empty filename"
        }), 400

    if not allowed_file(
        file.filename,
        current_app.config[
            "ALLOWED_EXTENSIONS"
        ]
    ):

        return jsonify({
            "success": False,
            "error":
                "Invalid file type"
        }), 400

    saved_file = save_uploaded_file(

        file,

        current_app.config[
            "RESUME_FOLDER"
        ]
    )

    return jsonify({

        "success": True,

        "message":
            "Resume uploaded successfully",

        "filename":
            saved_file["filename"]
    })