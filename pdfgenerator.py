import streamlit as st
from fpdf import FPDF
from io import BytesIO

st.title("Text to PDF Converter")
st.write("Enter your text below and convert it to a PDF file")

# Text area for user input
user_text = st.text_area(
    "Enter your text (one line per paragraph):",
    height=300,
    placeholder="Type or paste your content here...\nEach line will appear as a separate line in the PDF"
)

# Optional: Font size selector
font_size = st.slider("Select font size:", min_value=8, max_value=20, value=12)

# Optional: PDF filename
pdf_filename = st.text_input("PDF filename (without .pdf extension):", value="output")

# Convert button
if st.button("Convert to PDF"):
    if user_text:
        # Create instance of FPDF class
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=font_size)
        
        # Split the text into lines
        content = user_text.split('\n')
        
        # Write content to PDF
        for line in content:
            # Handle long lines by using multi_cell instead of cell
            pdf.multi_cell(190, 10, txt=line, align='L')
        
        # Save PDF to bytes buffer
        pdf_output = pdf.output(dest='S').encode('latin-1')
        
        # Create download button
        st.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name=f"{pdf_filename}.pdf",
            mime="application/pdf"
        )
        
        st.success("PDF generated successfully! Click the button above to download.")
    else:
        st.warning("Please enter some text first!")

