from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from model_dir.src.chord_savant import chord_recognition
# Initialize your Flask application:

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' #Change 1
# Create a route to handle the file upload and process it:

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the 'file' key is present in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'})
        
        audio_file = request.files['file']
        
        # Save the uploaded file to the UPLOAD_FOLDER directory
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(file_path)

        # Pass the audio file to your ML model for processing
        # Replace the following lines with your actual ML model code
        # output = your_ml_model(file_path)
        # For example, if your ML model is a function named `predict`:
        # output = predict(file_path)
        output = chord_recognition('/uploads')

        # Return the output to the frontend
        return jsonify({'result': output})

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)