from flask import Flask, render_template, request
import roboflow
import os
import tempfile
from werkzeug.utils import secure_filename
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not set in environment variables")

rf = roboflow.Roboflow(api_key=API_KEY)
project = rf.workspace("clashbot-artum").project("dollar-classify")
model = project.version(1).model

app = Flask(__name__)

# Max upload size (5 MB)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

# Allowed files
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def allowed_file(filename):
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)

@app.route('/')
def index():
    return render_template('index.html', predictions=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files or request.files['image'].filename == '':
        return render_template('index.html', predictions="No file selected.")

    file = request.files['image']

    if not allowed_file(file.filename):
        return render_template('index.html', predictions="Invalid file type. Only JPG, JPEG, PNG allowed.")

    filename = secure_filename(file.filename)

    try:
        # Save temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(filename)[1]) as tmp:
            file.save(tmp.name)
            temp_path = tmp.name

        # Get prediction from Roboflow
        prediction = model.predict(temp_path).json()
        preds = prediction.get("predictions", [])

        if preds:
            pred_text = ", ".join([f"{p['class']} ({p['confidence']*100:.1f}%)" for p in preds])
        else:
            pred_text = "No objects detected."

    except Exception as e:
        pred_text = f"Error: {str(e)}"

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return render_template('index.html', predictions=pred_text)

if __name__ == "__main__":
    app.run()