import streamlit as st
import uuid
import base64
import json
import os
import streamlit.components.v1 as components
from utils.ai import generate_professional_summary

STATE_FILE = "resume_state.json"

def init_session_state():
    if 'resume_data' not in st.session_state:
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, 'r') as f:
                    st.session_state.resume_data = json.load(f)
            except:
                st.session_state.resume_data = get_default_data()
        else:
            st.session_state.resume_data = get_default_data()

def get_default_data():
    return {
        'personal_info': {'name': '', 'title': '', 'email': '', 'phone': '', 'location': '', 'linkedin': '', 'github': '', 'portfolio': '', 'profile_pic': ''},
        'summary': '',
        'skills': [],
        'projects': [],
        'experience': [],
        'education': [],
        'certifications': [],
        'achievements': [],
        'customization': {
            'accent_color': '#2563eb',
            'font_family': 'Arial, sans-serif',
            'font_size': '14px',
            'line_spacing': '1.5',
            'page_margin': '40px',
            'template': 'Modern ATS',
            'show_certifications': True,
            'show_achievements': True
        }
    }

def save_state():
    with open(STATE_FILE, 'w') as f:
        json.dump(st.session_state.resume_data, f)

def update_personal_info(key):
    st.session_state.resume_data['personal_info'][key] = st.session_state[f'pi_{key}']

def update_summary():
    st.session_state.resume_data['summary'] = st.session_state['summary_input']

def generate_summary():
    data = st.session_state.resume_data
    skills_str = ", ".join([s for cat in data['skills'] for s in cat['items']])
    exp_str = ", ".join([f"{e['role']} at {e['company']}" for e in data['experience']])
    edu_str = ", ".join([f"{e['degree']} from {e['institute']}" for e in data['education']])
    proj_str = ", ".join([p['name'] for p in data['projects']])
    
    with st.spinner("Generating summary..."):
        summary = generate_professional_summary(
            name=data['personal_info']['name'],
            title=data['personal_info']['title'],
            skills=skills_str,
            experience=exp_str,
            education=edu_str,
            projects=proj_str
        )
        st.session_state.resume_data['summary'] = summary
        st.session_state['summary_input'] = summary

def add_item(category, template):
    st.session_state.resume_data[category].append(template)

def remove_item(category, index):
    st.session_state.resume_data[category].pop(index)

def render_form():
    init_session_state()
    data = st.session_state.resume_data
    
    st.markdown("### Build Your Resume")
    
    # --- CUSTOMIZATION ---
    with st.expander("Customization & Templates", expanded=False):
        template_options = ["Modern ATS", "Two Column", "Minimal Premium"]
        st.selectbox("Template", template_options, key="cust_template", 
                     index=template_options.index(data['customization']['template']),
                     on_change=lambda: st.session_state.resume_data['customization'].update({'template': st.session_state.cust_template}))
        
        col1, col2 = st.columns(2)
        with col1:
            st.color_picker("Accent Color", value=data['customization']['accent_color'], key="cust_color",
                            on_change=lambda: st.session_state.resume_data['customization'].update({'accent_color': st.session_state.cust_color}))
            st.selectbox("Font Family", ["Arial, sans-serif", "Helvetica, sans-serif", "Georgia, serif", "Times New Roman, serif", "Inter, sans-serif", "Roboto, sans-serif"], key="cust_font",
                         index=0, on_change=lambda: st.session_state.resume_data['customization'].update({'font_family': st.session_state.cust_font}))
        with col2:
            st.selectbox("Font Size", ["12px", "13px", "14px", "15px", "16px"], key="cust_size", index=2,
                         on_change=lambda: st.session_state.resume_data['customization'].update({'font_size': st.session_state.cust_size}))
            st.selectbox("Line Spacing", ["1.2", "1.4", "1.5", "1.6", "1.8"], key="cust_line", index=2,
                         on_change=lambda: st.session_state.resume_data['customization'].update({'line_spacing': st.session_state.cust_line}))
        
        st.selectbox("Page Margin", ["20px", "30px", "40px", "50px", "60px"], key="cust_margin", index=2,
                     on_change=lambda: st.session_state.resume_data['customization'].update({'page_margin': st.session_state.cust_margin}))
                     
        st.checkbox("Show Certifications", value=data['customization']['show_certifications'], key="cust_cert",
                    on_change=lambda: st.session_state.resume_data['customization'].update({'show_certifications': st.session_state.cust_cert}))
        st.checkbox("Show Achievements", value=data['customization']['show_achievements'], key="cust_ach",
                    on_change=lambda: st.session_state.resume_data['customization'].update({'show_achievements': st.session_state.cust_ach}))
                    
        if st.button("Reset Resume"):
            del st.session_state.resume_data
            st.rerun()

    # --- PERSONAL INFO ---
    with st.expander("Personal Information", expanded=True):
        pi = data['personal_info']
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Full Name", value=pi['name'], key="pi_name", on_change=update_personal_info, args=('name',))
            st.text_input("Email", value=pi['email'], key="pi_email", on_change=update_personal_info, args=('email',))
            st.text_input("Location", value=pi['location'], key="pi_location", on_change=update_personal_info, args=('location',))
            st.text_input("GitHub URL", value=pi['github'], key="pi_github", on_change=update_personal_info, args=('github',))
        with col2:
            st.text_input("Professional Title", value=pi['title'], key="pi_title", on_change=update_personal_info, args=('title',))
            st.text_input("Phone Number", value=pi['phone'], key="pi_phone", on_change=update_personal_info, args=('phone',))
            st.text_input("LinkedIn URL", value=pi['linkedin'], key="pi_linkedin", on_change=update_personal_info, args=('linkedin',))
            st.text_input("Portfolio Website", value=pi['portfolio'], key="pi_portfolio", on_change=update_personal_info, args=('portfolio',))
        
        st.markdown("<br><b>Profile Picture</b>", unsafe_allow_html=True)
        if pi.get('profile_pic'):
            col_img, col_btn = st.columns([1, 3])
            with col_img:
                st.markdown(f'<img src="{pi["profile_pic"]}" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #e2e8f0;">', unsafe_allow_html=True)
            with col_btn:
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("Remove Photo", key="btn_remove_photo"):
                    st.session_state.resume_data['personal_info']['profile_pic'] = ""
                    st.rerun()
        
        uploaded_file = st.file_uploader("Upload New Photo (Optional)", type=['png', 'jpg', 'jpeg'], key="pi_pic_upload")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            base64_str = base64.b64encode(bytes_data).decode('utf-8')
            st.session_state.resume_data['personal_info']['profile_pic'] = f"data:{uploaded_file.type};base64,{base64_str}"

    # --- SUMMARY ---
    with st.expander("Professional Summary"):
        st.text_area("Summary", value=data['summary'], key="summary_input", on_change=update_summary, height=150)
        st.button("Generate with AI", on_click=generate_summary)

    # --- SKILLS ---
    with st.expander("Skills"):
        for i, cat in enumerate(data['skills']):
            st.markdown(f"**Category {i+1}**")
            def update_skill_name(idx=i):
                st.session_state.resume_data['skills'][idx]['name'] = st.session_state[f'skill_name_{idx}']
            def update_skill_items(idx=i):
                items = [s.strip() for s in st.session_state[f'skill_items_{idx}'].split(',') if s.strip()]
                st.session_state.resume_data['skills'][idx]['items'] = items
                
            st.text_input("Category Name (e.g. Programming Languages)", value=cat['name'], key=f"skill_name_{i}", on_change=update_skill_name)
            st.text_input("Skills (comma separated)", value=", ".join(cat['items']), key=f"skill_items_{i}", on_change=update_skill_items)
            if st.button("Remove Category", key=f"rm_skill_{i}"):
                remove_item('skills', i)
                st.rerun()
            st.divider()
            
        if st.button("Add Skill Category"):
            add_item('skills', {'name': '', 'items': []})
            st.rerun()

    # --- EXPERIENCE ---
    with st.expander("Experience"):
        for i, exp in enumerate(data['experience']):
            st.markdown(f"**Experience {i+1}**")
            def update_exp(k, idx=i):
                st.session_state.resume_data['experience'][idx][k] = st.session_state[f'exp_{k}_{idx}']
            
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Company", value=exp['company'], key=f"exp_company_{i}", on_change=update_exp, args=('company',))
                st.text_input("Duration", value=exp['duration'], key=f"exp_duration_{i}", on_change=update_exp, args=('duration',))
            with col2:
                st.text_input("Role", value=exp['role'], key=f"exp_role_{i}", on_change=update_exp, args=('role',))
            
            st.text_area("Description", value=exp['description'], key=f"exp_description_{i}", on_change=update_exp, args=('description',))
            if st.button("Remove Experience", key=f"rm_exp_{i}"):
                remove_item('experience', i)
                st.rerun()
            st.divider()

        if st.button("Add Experience"):
            add_item('experience', {'company': '', 'role': '', 'duration': '', 'description': ''})
            st.rerun()

    # --- EDUCATION ---
    with st.expander("Education"):
        for i, edu in enumerate(data['education']):
            st.markdown(f"**Education {i+1}**")
            def update_edu(k, idx=i):
                st.session_state.resume_data['education'][idx][k] = st.session_state[f'edu_{k}_{idx}']
            
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("Institute", value=edu['institute'], key=f"edu_institute_{i}", on_change=update_edu, args=('institute',))
                st.text_input("Branch/Major", value=edu['branch'], key=f"edu_branch_{i}", on_change=update_edu, args=('branch',))
                st.text_input("Start Year", value=edu['start_year'], key=f"edu_start_year_{i}", on_change=update_edu, args=('start_year',))
            with col2:
                st.text_input("Degree", value=edu['degree'], key=f"edu_degree_{i}", on_change=update_edu, args=('degree',))
                st.text_input("CGPA", value=edu['cgpa'], key=f"edu_cgpa_{i}", on_change=update_edu, args=('cgpa',))
                st.text_input("End Year", value=edu['end_year'], key=f"edu_end_year_{i}", on_change=update_edu, args=('end_year',))
                
            if st.button("Remove Education", key=f"rm_edu_{i}"):
                remove_item('education', i)
                st.rerun()
            st.divider()

        if st.button("Add Education"):
            add_item('education', {'institute': '', 'degree': '', 'branch': '', 'start_year': '', 'end_year': '', 'cgpa': ''})
            st.rerun()

    # --- PROJECTS ---
    with st.expander("Projects"):
        for i, proj in enumerate(data['projects']):
            st.markdown(f"**Project {i+1}**")
            def update_proj(k, idx=i):
                st.session_state.resume_data['projects'][idx][k] = st.session_state[f'proj_{k}_{idx}']
            
            st.text_input("Project Name", value=proj['name'], key=f"proj_name_{i}", on_change=update_proj, args=('name',))
            st.text_input("Technologies Used", value=proj['technologies'], key=f"proj_technologies_{i}", on_change=update_proj, args=('technologies',))
            col1, col2 = st.columns(2)
            with col1:
                st.text_input("GitHub Link", value=proj['github'], key=f"proj_github_{i}", on_change=update_proj, args=('github',))
            with col2:
                st.text_input("Live Demo", value=proj['demo'], key=f"proj_demo_{i}", on_change=update_proj, args=('demo',))
            st.text_area("Description", value=proj['description'], key=f"proj_description_{i}", on_change=update_proj, args=('description',))
            
            if st.button("Remove Project", key=f"rm_proj_{i}"):
                remove_item('projects', i)
                st.rerun()
            st.divider()

        if st.button("Add Project"):
            add_item('projects', {'name': '', 'technologies': '', 'github': '', 'demo': '', 'description': ''})
            st.rerun()
            
    # --- CERTIFICATIONS & ACHIEVEMENTS ---
    with st.expander("Certifications & Achievements"):
        def update_list(category):
            st.session_state.resume_data[category] = [x.strip() for x in st.session_state[f'{category}_input'].split('\n') if x.strip()]
        
        st.text_area("Certifications (one per line)", value="\n".join(data['certifications']), key="certifications_input", on_change=update_list, args=('certifications',))
        st.text_area("Achievements (one per line)", value="\n".join(data['achievements']), key="achievements_input", on_change=update_list, args=('achievements',))

    # Auto-save state to disk on every render
    save_state()
    
    # Inject JavaScript to make 'Enter' focus the next input field
    components.html(
        """
        <script>
        const doc = window.parent.document;
        doc.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && e.target.tagName === 'INPUT') {
                const inputs = Array.from(doc.querySelectorAll('input[type="text"]'));
                const index = inputs.indexOf(e.target);
                if (index > -1 && index < inputs.length - 1) {
                    inputs[index + 1].focus();
                    e.preventDefault();
                }
            }
        });
        </script>
        """,
        height=0,
        width=0
    )

    return data
