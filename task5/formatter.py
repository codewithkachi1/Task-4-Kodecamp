def format_resume(resume_data):
    resume = f"# {resume_data['name']}\n\n"
    resume += f"Email: {resume_data['email']}\n"
    resume += f"Phone: {resume_data['phone']}\n\n"
    resume += f"{resume_data['summary']}\n\n"

    resume += "## Education\n"
    for education in resume_data['education']:
        resume += f"* {education['degree']}, {education['university']}, {education['graduation_date']}\n"
    resume += "\n"

    resume += "## Work Experience\n"
    for experience in resume_data['work_experience']:
        resume += f"* {experience['job_title']}, {experience['company']}, {experience['employment_dates']}\n"
        for responsibility in experience['responsibilities']:
            resume += f"  + {responsibility}\n"
    resume += "\n"

    resume += "## Skills\n"
    for skill in resume_data['skills']:
        resume += f"* {skill}\n"

    return resume

def format_resume_txt(resume_data):
    resume = f"{resume_data['name']}\n"
    resume += f"Email: {resume_data['email']}\n"
    resume += f"Phone: {resume_data['phone']}\n\n"
    resume += f"{resume_data['summary']}\n\n"

    resume += "Education:\n"
    for education in resume_data['education']:
        resume += f"* {education['degree']}, {education['university']}, {education['graduation_date']}\n"
    resume += "\n"

    resume += "Work Experience:\n"
    for experience in resume_data['work_experience']:
        resume += f"* {experience['job_title']}, {experience['company']}, {experience['employment_dates']}\n"
        for responsibility in experience['responsibilities']:
            resume += f"  + {responsibility}\n"
    resume += "\n"

    resume += "Skills:\n"
    for skill in resume_data['skills']:
        resume += f"* {skill}\n"

    return resume