import os
import re
import csv
from PyPDF2 import PdfReader
from collections import Counter

# Get role selection from user
def select_roles():
    # Prompt the user for role selection
    available_roles = ["Software Developer", "Data Analyst", "Project Manager"]
    print("Available Roles:")
    for i, role in enumerate(available_roles, 1):
        print(f"{i}. {role}")
    selected_roles = input("Enter the numbers of the roles you'd like to screen (comma-separated): ")
    selected_roles = [available_roles[int(i) - 1] for i in selected_roles.split(",") if i.isdigit()]
    print(f"\nSelected Roles: {', '.join(selected_roles)}")
    return selected_roles

# Get skills for each selected role from the user
def get_skills_for_roles(selected_roles):
    role_skills = {}
    for role in selected_roles:
        skills = input(f"Enter the skills required for {role} (comma-separated): ")
        role_skills[role] = [skill.strip().lower() for skill in skills.split(",")]
    return role_skills

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

# Analyze resumes for selected roles and calculate scores
def screen_resumes(resume_folder, selected_roles, role_skills):
    screened_results = []
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(filepath)
            
            role_data = {role: 0 for role in selected_roles}  # Initialize scores for each selected role
            matched_skills = {role: [] for role in selected_roles}  # Track matched skills
            
            # Check for skills in each selected role
            for role in selected_roles:
                skills = role_skills[role]
                role_count = Counter(word for word in text.split() if word in skills)
                role_data[role] = sum(role_count.values())
                matched_skills[role] = [skill for skill in skills if skill in role_count]

            # Append result for this resume
            screened_results.append({
                "filename": filename,
                "role_data": role_data,
                "matched_skills": matched_skills
            })
    return screened_results

# Manual selection of resumes
def manual_selection(screened_results):
    selected_candidates = []
    not_selected_candidates = []

    for result in screened_results:
        print(f"\nResume: {result['filename']}")
        for role, score in result["role_data"].items():
            print(f"Role: {role}, Score: {score}, Skills Matched: {', '.join(result['matched_skills'][role])}")
        
        # User decides selection
        choice = input("Select this resume for any role? (y/n): ").strip().lower()
        if choice == "y":
            selected_candidates.append(result)
        else:
            not_selected_candidates.append(result)

    return selected_candidates, not_selected_candidates

# Export results to CSV
def export_results(selected, not_selected):
    with open("screening_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Role", "Score", "Skills Matched", "Status"])

        for result in selected:
            for role, score in result["role_data"].items():
                writer.writerow([result["filename"], role, score, ", ".join(result["matched_skills"][role]), "Selected"])
        
        for result in not_selected:
            for role, score in result["role_data"].items():
                writer.writerow([result["filename"], role, score, ", ".join(result["matched_skills"][role]), "Not Selected"])

    print("Results exported to 'screening_results.csv'")

# Main program
if __name__ == "__main__":
    resume_folder = "resumes"  # Folder where resumes are stored
    selected_roles = select_roles()  # User selects roles
    role_skills = get_skills_for_roles(selected_roles)  # User inputs skills for each role
    screened_results = screen_resumes(resume_folder, selected_roles, role_skills)
    selected, not_selected = manual_selection(screened_results)
    export_results(selected, not_selected)
