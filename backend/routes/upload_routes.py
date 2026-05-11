from flask import Blueprint

from controllers.upload_controller import (
    upload_resume_controller
)

upload_bp = Blueprint(
    "upload_bp",
    __name__
)

# ----------------------------------

@upload_bp.route(
    "/upload",
    methods=["POST"]
)
def upload():

    return upload_resume_controller()