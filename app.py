from flask import Flask,request,jsonify
from dotenv import load_dotenv
import os
import json
from controllers.pdf_controllers import PDFController
import fitz
load_dotenv()

app = Flask(__name__)
PORT = os.getenv('PORT')

@app.get("/")
def ok():
    return "Test-1"

@app.route("/get_fields",methods=["POST"])
def get_fields_from_pdf():
    file = request.files["file"]
    
    obj = PDFController(file)
    try:
         return obj._get_fields()
    except Exception as e:
         return jsonify({"error":str(e)})
 

@app.route("/update_field",methods=["PUT"])
def update_field():
    file = request.files["file"]
    field =json.loads(request.form["field"])
    print(field.get("hi"))
    try:
        obj = PDFController(file) 
        return obj._update_pdf(field)
    except Exception as e:
        return jsonify({"error":str(e)})

@app.route("/update_fields",methods=["PUT"])
def update_multiple_fields():
    file = request.files["file"]
    fields = json.loads(request.form["fields"])
    print("fields",fields)
    try:
        obj=PDFController(file)
        return obj._update_fields(fields)
    except Exception as e:
        return jsonify({"error":str(e)})
    
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=PORT,debug=True)