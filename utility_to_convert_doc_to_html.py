# Perform pip install mammoth

import mammoth

with open("introduction_to_python.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value  
    with open("introduction_to_python.html", "w", encoding="utf-8") as html_file:
        html_file.write(html)

print("Conversion complete: introduction_to_python.html")
