def get_personal_details():
    print("Enter Personal Details:")
    name = input("Full Name: ")
    email = input("Email Address: ")
    phone = input("Phone Number: ")
    summary = input("Professional Summary: ")
    return {'name': name, 'email': email, 'phone': phone, 'summary': summary}

def get_education_details():
    print("Enter Educational Background:")
    education = []
    while True:
        degree = input("Degree (e.g., BSc Computer Science): ")
        institution = input("Institution Name: ")
        graduation_year = input("Graduation Year: ")
        education.append({'degree': degree, 'institution': institution, 'graduation_year': graduation_year})
        add_more = input("Add another education? (yes/no): ").lower()
        if add_more != 'yes':
            break
    return education

def get_work_experience():
    print("Enter Work Experience:")
    experience = []
    while True:
        company = input("Company Name: ")
        job_title = input("Job Title: ")
        role = input("Role Description: ")
        experience.append({'company': company, 'job_title': job_title, 'role': role})
        add_more = input("Add another experience? (yes/no): ").lower()
        if add_more != 'yes':
            break
    return experience

def get_skills():
    print("Enter Skills:")
    skills = input("List of Skills (comma-separated): ").split(',')
    return [skill.strip() for skill in skills]

def generate_resume(personal_details, education, experience, skills):
    print("\nGenerated Resume:")
    print("===================================")
    print(f"Name: {personal_details['name']}")
    print(f"Email: {personal_details['email']}")
    print(f"Phone: {personal_details['phone']}")
    print(f"\nProfessional Summary:\n{personal_details['summary']}")
    
    print("\nEducation:")
    for edu in education:
        print(f"- {edu['degree']} from {edu['institution']}, {edu['graduation_year']}")
        
    print("\nWork Experience:")
    for exp in experience:
        print(f"- {exp['job_title']} at {exp['company']}: {exp['role']}")
        
    print("\nSkills:")
    for skill in skills:
        print(f"- {skill}")
    print("===================================")

def main():
    print("Welcome to Resume Builder App!")
    personal_details = get_personal_details()
    education = get_education_details()
    experience = get_work_experience()
    skills = get_skills()
    
    generate_resume(personal_details, education, experience, skills)

if __name__ == "__main__":
    main()
