Resume Filter Tool
Overview
The Resume Filter Tool is a Python-based application designed to help HR professionals and recruiters filter, sort, and analyze resumes more efficiently. It uses Natural Language Processing (NLP) and machine learning techniques to match resumes against job descriptions, ensuring a quicker, more accurate screening process.

Features
Resume Parsing: Extracts key information from resumes (such as name, skills, experience, education, etc.).
Skill Matching: Compares the skills listed in resumes with those mentioned in job descriptions.
Score-Based Filtering: Ranks resumes based on how well they match a given job description.
Search and Sorting: Filters resumes by keywords, skills, experience, and other criteria.
User-Friendly Interface: A simple command-line interface (CLI) for inputting job descriptions and uploading resumes.
Tech Stack
Python 3.x: Core programming language used.
Libraries:
pandas for data handling.
nltk and spaCy for text preprocessing.
sklearn for machine learning models.
docx, PyPDF2, and other tools for resume parsing.
Installation
Prerequisites
Make sure you have Python 3.x installed. You will also need to install the required dependencies.

bash
Copy
Edit
pip install -r requirements.txt
Setup Instructions
Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/resume-filter-tool.git
cd resume-filter-tool
Install required libraries:
bash
Copy
Edit
pip install -r requirements.txt
Run the tool:
bash
Copy
Edit
python main.py
Usage
Input your job description: The tool will prompt you to paste the job description.
Upload Resumes: Upload one or more resumes (in PDF, DOCX, or TXT formats).
Filter and Sort: The tool will process the resumes, score them based on how well they match the job description, and output the results.
Review the Results: View the top matches ranked by score, with key information extracted from the resumes.
Example
bash
Copy
Edit
Job Description: Software Developer with expertise in Python, JavaScript, and SQL.

Please upload resumes: resume1.pdf, resume2.docx
Output:

yaml
Copy
Edit
Resume 1: Score: 85%
Skills Matched: Python, JavaScript, SQL
Experience: 3 years in software development
Education: B.Tech in Computer Science

Resume 2: Score: 70%
Skills Matched: Python, SQL
Experience: 2 years in software development
Education: B.Sc. in Information Technology
Contributing
Feel free to fork this project and submit issues and pull requests. All contributions are welcome!

Fork the repository
Create your feature branch (git checkout -b feature-name)
Commit your changes (git commit -am 'Add feature')
Push to the branch (git push origin feature-name)
Create a new Pull Request
