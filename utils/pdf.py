from playwright.sync_api import sync_playwright
import tempfile
import os

def generate_pdf_from_html(html_content: str) -> str:
    """
    Takes an HTML string, renders it in a headless Chromium browser using Playwright,
    and returns the file path to the generated PDF.
    """
    # Create a temporary file for the PDF
    fd, pdf_path = tempfile.mkstemp(suffix=".pdf")
    os.close(fd)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Load the HTML content directly
        page.set_content(html_content, wait_until="networkidle")
        
        # Generate the PDF
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        browser.close()
        
    return pdf_path
