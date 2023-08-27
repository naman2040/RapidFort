import os
from flask import Flask, request, jsonify, render_template, make_response
from flask_restful import Api, Resource
import magic

app = Flask(__name__, template_folder='F:\Visual Studio\RapidFort\\templates')
api = Api(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

@app.route('/upload', methods=['GET'])
def upload_form():
    return render_template('page.html')

class UploadFile(Resource):
    def get(self):
        return render_template('page.html')

    def post(self):
        file = request.files['file']
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            file_info = magic.from_file(file_path)
            mime_type = magic.from_file(file_path, mime=True)
            data = {
                "file_name": file.filename,
                "info": file_info,
                "mime_type": mime_type
            }
            rendered = render_template('page.html',data=data)
            return make_response(rendered,200,{'content-Type':'text/html'})
        else:
            return {"error": "File not provided"}, 400

api.add_resource(UploadFile, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
