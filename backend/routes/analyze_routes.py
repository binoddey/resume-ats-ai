from flask import Blueprint

from controllers.analyze_controller import (
    analyze_resume_controller
)

analyze_bp = Blueprint(
    "analyze_bp",
    __name__
)

# ----------------------------------

@analyze_bp.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    return analyze_resume_controller()