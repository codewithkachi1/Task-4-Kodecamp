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