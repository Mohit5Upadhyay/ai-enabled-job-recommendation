import streamlit as st
from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_linkedin_jobs , fetch_naukri_jobs


st.set_page_config(page_title="Job Recommender", layout="wide")
st.title("AI powered Job Recommender")
st.markdown("Upload your resume and get job recommendations based on your skills and experience from linkedIn.com and naukri.com")

uploaded_file = st.file_uploader("Upload your latest resume (PDF)", type=["pdf"])

if uploaded_file:
    # loading state..
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    # resume summary
    with st.spinner("Summarizing your resume..."):
        summary = ask_openai(f"Summarize this resume highlighting the skills, education, and experience ,achivements: \n\n{resume_text}", max_tokens=500)

    # skill gaps and roadmap
    with st.spinner("Finding skill Gaps..."):
        gaps = ask_openai(f"Analyze this resume and highlight missing skills, certifications, and experiences needed for better job opportunities in the pointers: \n\n{resume_text}", max_tokens=400)

    # future roadmap
    with st.spinner("Creating Future Roadmap..."):
        roadmap = ask_openai(f"Based on this resume, suggest a future roadmap to improve the person's career prospects (Skill to learn, certification needed, industry exposure , free courses) provide future roadmap in pointers in hirearchial manner: \n\n{resume_text}", max_tokens=400)
    
    # Display nicely formatted results
    st.markdown("---")
    st.header("📑 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html=True)

    st.success("✅ Analysis Completed Successfully!")


    if st.button("🔎Get Job Recommendations"):
        with st.spinner("Fetching related jobs..."):
            keywords = ask_openai(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma-separated list ONLY, NO Explanation.\n\nSummary: {summary}",
                max_tokens=100
            )

            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Extracted Job Keywords from Resume/CV: {search_keywords_clean}")

        with st.spinner("Fetching jobs from LinkedIn and Naukri..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=60)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)


        st.markdown("---")
        st.header("💼 Top LinkedIn Jobs -->")

        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No LinkedIn jobs found.")






        st.markdown("---")
        st.header("💼 Top Naukri Jobs (India)")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Naukri jobs found.")

