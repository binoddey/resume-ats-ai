import os
import uuid

def allowed_file(filename, allowed_extensions):

    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower()
        in allowed_extensions
    )

def generate_unique_filename(filename):

    extension = filename.rsplit(".", 1)[1]

    unique_name = f"{uuid.uuid4()}.{extension}"

    return unique_name

def save_uploaded_file(
    file,
    upload_folder
):

    filename = generate_unique_filename(
        file.filename
    )

    filepath = os.path.join(
        upload_folder,
        filename
    )

    file.save(filepath)

    return {
        "filename": filename,
        "filepath": filepath
    }