import json
import formatter

# filename = "resume.json"
def load_resume(filename):
    with open(filename, "r") as file:
        return json.load(file)

def save_resume(resume_data, filename, format="md"):
    if format == "md":
        resume = formatter.format_resume(resume_data)
    elif format == "txt":
        resume = formatter.format_resume_txt(resume_data)
    else:
        raise ValueError("Invalid format")

    with open(filename, "w") as file:
        file.write(resume)

def main():
    resume_data = load_resume("task5/resume.json")
    save_resume(resume_data, "resume.md", format="md")
    save_resume(resume_data, "resume.txt", format="txt")

main()


# README.md

# # Resume Generator

# This project generates a resume from structured_data stored in JSON format.

# ### Features
# * Loads resume data from `resume.json`
# * Generates resume in Markdown and plain text formats
# * Saves generated resumes to `resume.md` and `resume.txt`

# ### Usage
# 1. Update `resume.json` with your personal data
# 2. Run `python resume.py` to generate resumes


# You can upload these files to GitHub and use the resume generator to create your own resume. Make sure to update the resume.json file with your own data.