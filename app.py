import streamlit as st
import os
from components.sidebar import render_form
from components.preview import render_preview
from components.export import render_export
from utils.ai import generate_cover_letter

# Must be the first Streamlit command
st.set_page_config(page_title="AI Career Suite", layout="wide")

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "static", "styles.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css()
    
    # Inject Custom Header (Navbar)
    st.markdown(
        """
        <div class="custom-navbar">
            <div class="navbar-brand">
                <i class="fa-solid fa-briefcase"></i>
                AI Career Suite
            </div>
            <div class="navbar-links">
                <span class="nav-link"><i class="fa-solid fa-rocket"></i> Premium</span>
                <span class="nav-link"><i class="fa-solid fa-life-ring"></i> Support</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<h2 style='margin-top: -20px; color: #1e293b;'>Professional Resume Builder</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748b; font-size: 1.1em;'>Craft tailored resumes and cover letters to stand out.</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Resume Builder", "Cover Letter Generator"])
    
    with tab1:
        # We split the page 60/40 for the Resume Builder
        col_form, col_preview = st.columns([6, 4])
        
        with col_form:
            # Render the form (previously in the sidebar)
            resume_data = render_form()
            
        with col_preview:
            # Render Live HTML Preview on the right
            render_preview(resume_data)
        
        # Render Export section below the preview
        render_export(resume_data)

    with tab2:
        st.markdown("### Generate Cover Letter")
        st.markdown("Enter the job role you are applying for. We'll automatically pull your Name, Skills, and Experience from your Resume Builder profile to craft a tailored cover letter.")
        
        job_role = st.text_input("Job Role Applying For (e.g. Senior Frontend Developer)")
        
        if st.button("Generate Cover Letter", type="primary"):
            if 'resume_data' not in st.session_state:
                st.warning("Please fill out your Personal Info and Experience in the Resume Builder first!")
            elif not job_role:
                st.warning("Please enter a Job Role.")
            else:
                data = st.session_state.resume_data
                name = data['personal_info'].get('name', 'Applicant')
                skills_str = ", ".join([s for cat in data['skills'] for s in cat['items']])
                exp_str = ", ".join([f"{e['role']} at {e['company']}" for e in data['experience']])
                
                with st.spinner("Writing your cover letter..."):
                    letter = generate_cover_letter(
                        name=name,
                        job_role=job_role,
                        skills=skills_str,
                        experience=exp_str
                    )
                    st.session_state['generated_letter'] = letter
                    
        if 'generated_letter' in st.session_state:
            st.markdown("---")
            st.markdown("#### Your Cover Letter")
            st.text_area("You can edit or copy it directly below:", value=st.session_state['generated_letter'], height=400)
            
            st.download_button(
                label="Download Cover Letter as .txt",
                data=st.session_state['generated_letter'],
                file_name="Cover_Letter.txt",
                mime="text/plain"
            )

    # Inject Custom Footer
    st.markdown(
        """
        <div class="custom-footer">
            <p>&copy; 2026 AI Career Suite. Crafted with <i class="fa-solid fa-heart" style="color:#ec4899;"></i> for modern professionals.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
