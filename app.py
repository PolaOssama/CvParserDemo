from flask import Flask, request, jsonify, render_template
import model as f
import os
import base64
from flask import jsonify

UPLOAD_FOLDER = 'cvparser\\CVs\\'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

app = Flask(__name__,static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    filee = request.files['file']
   
    filename=filee.name

    filee.save(os.path.join(app.config['UPLOAD_FOLDER'], filee.filename))

    f.namee(filee.filename) 
    #return jsonify(f.data)
    
 
    
    return jsonify(num = f.namee(filee.filename))

if __name__ == "__main__":
    app.run(debug=True)
    
