from flask import Blueprint,render_template,jsonify,request
from .analyzer import Convert_pdf_into_text,analyze_resume
import os,json
import asyncio
import aiofiles

main_bp= Blueprint('main',__name__)

SAVE_UPLOADED_FILE = os.getenv('SAVE_UPLOADED_FILE')
ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS')

@main_bp.route("/")
@main_bp.route("/homepage.html")
def homepage_method():
    return render_template("homepage.html")

@main_bp.route("/page_settings.html")
def page_settings_method():
    return render_template("page_settings.html")

@main_bp.route("/themes.html")
def themes_method():
    return render_template("themes.html")

def check_allowed_file(filename):
 return "." in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route("/upload",methods=['POST'])
def upload():

    try:
        if 'resume' not in request.files:
            return jsonify({
            "message" : "please select and file an submit the file",
            "status" : "success",
            "versioN": "1.0"
        })
        file = request.files['resume']
        
        if file and check_allowed_file(file.filename):
        
            new_filename = file.filename

            #    upload_path = os.path.join(SAVE_UPLOADED_FILE, new_filename)
            #    os.makedirs(SAVE_UPLOADED_FILE, exist_ok=True)

            #    save_file = asyncio.create_task(save_file_async(SAVE_UPLOADED_FILE, file))
            
            # Save the file
            ##file.save(upload_path)

            file_content = Convert_pdf_into_text(file)

            if file_content : 
                # reponse = json.loads(analyze_resume(file_content))
                reponse = analyze_resume(file_content)
            else:
                    return jsonify({
                            "message" : "helo world in json format",
                            "status" : "success",
                            "versioN": "1.0"
                        })   

            return jsonify({
                    "message" : reponse,
                    "status" : "success",
                    "versioN": "1.0"
                })
        else:
            return jsonify({
                "message" : "Uploaded file is in improper format ",
                "status" : "success",
                "versioN": "1.0"
            })
    except Exception as e :
                return jsonify({
        "message" : "Internal Server Error",
        "status" : "success",
        "versioN": "1.0"
                })

async def save_file_async(filepath:str,file):
   try:
      async with aiofiles.open(filepath,'wb') as f:
            content = await f.read()
            await f.write(content)
      return True
   except Exception as e:
    return False



@main_bp.route("/api/hlojson")
def json_hllo_wrld():
    return jsonify({
        "message" : "helo world in json format",
        "status" : "success",
        "version" : "1.0"
    })