import streamlit as st
import os
from components.preview import get_html_for_template
from utils.pdf import generate_pdf_from_html

def render_export(data):
    st.markdown("<br><hr style='border-top: 1px dashed #9dbdba; margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)
    st.markdown("### Export Your Resume")
    st.markdown("Download your finalized resume in a high-quality PDF format. Ready to impress recruiters!")
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Prepare PDF for Download", type="primary", use_container_width=True):
        with st.spinner("Rendering PDF... This may take a few seconds."):
            try:
                html = get_html_for_template(data)
                
                # Wrap the HTML in standard html tags with styles.css if needed, 
                # but the templates already include <style> and <html> tags.
                full_html = html
                
                pdf_path = generate_pdf_from_html(full_html)
                
                with open(pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                    
                st.markdown("<br>", unsafe_allow_html=True)
                st.success("PDF generated successfully! Click below to download your file.")
                
                st.download_button(
                    label="Download PDF Now",
                    data=pdf_bytes,
                    file_name=f"{data['personal_info']['name'].replace(' ', '_')}_Resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
                
                # Clean up
                os.remove(pdf_path)
            except Exception as e:
                st.error(f"Failed to generate PDF: {str(e)}")
