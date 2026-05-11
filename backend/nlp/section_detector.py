def detect_sections(text):

    text = text.lower()

    known_sections = [

        "education",

        "skills",

        "projects",

        "experience",

        "certifications",

        "summary",

        "achievements",

        "leadership"
    ]

    found_sections = []

    for section in known_sections:

        if section in text:

            found_sections.append(section)

    return found_sections