import streamlit as st
import streamlit.components.v1 as components
from templates.modern import get_modern_template
from templates.twocolumn import get_twocolumn_template
from templates.minimal import get_minimal_template

def get_html_for_template(data):
    template_name = data['customization']['template']
    if template_name == 'Two Column':
        return get_twocolumn_template(data)
    elif template_name == 'Minimal Premium':
        return get_minimal_template(data)
    else:
        return get_modern_template(data)

def render_preview(data):
    html_content = get_html_for_template(data)
    
    st.markdown("### Live Preview")
    
    # Hidden anchor to target this specific iframe in CSS
    st.markdown("<div id='preview-anchor'></div>", unsafe_allow_html=True)
    
    components.html(
        html_content,
        height=700, 
        scrolling=True
    )
