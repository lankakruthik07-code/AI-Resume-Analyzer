def analyze_resume(resume, job_description):
    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    matched_skills = resume_words.intersection(job_words)
    missing_skills = job_words - resume_words

    match_percentage = (len(matched_skills) / len(job_words)) * 100

    return matched_skills, missing_skills, match_percentage


resume_text = input("Paste your resume text: ")
job_desc = input("Paste job description: ")

matched, missing, match = analyze_resume(resume_text, job_desc)

print("\nMatched Skills:", matched)
print("\nMissing Skills:", missing)
print(f"\nResume Match: {match:.2f}%")
