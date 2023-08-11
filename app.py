from flask import Flask, request, render_template
from docx import Document
import time

app = Flask(__name__)

# In-memory storage for embeddings (simulated for the example)
document_embeddings = []

def docx_to_text(file):
    """Converts the DOCX file to plain text."""
    doc = Document(file)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route that handles both the display of the upload form and the processing of uploaded files."""
    message = ""
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files.get('file')
        
        if file and file.filename:
            # Convert the document to text
            text = docx_to_text(file)
            
            # Simulate delays for the sake of progress demonstration
            time.sleep(2)  # Simulating the time taken for breaking into pieces
            time.sleep(2)  # Simulating the time taken for generating embeddings
            time.sleep(2)  # Simulating the time taken for additional processing
            
            # This is a placeholder for actual embeddings
            embedding = [1, 2, 3]
            document_embeddings.append(embedding)

            message = "File uploaded and processed!"

    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
