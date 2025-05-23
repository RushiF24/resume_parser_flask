import os
import json
import uuid
from flask import Blueprint, render_template, request
from base.com.dao.candidated_dao import CandidateDAO
from base.com.utils.helpers import extract_text_from_pdf
from base.com.services.gemini_service import parse_resume

candidate_blueprint = Blueprint('candidate_blueprint', __name__, url_prefix='/candidates')

UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@candidate_blueprint.route('/')
def Home():
    candidate_dao = CandidateDAO()
    results = candidate_dao.get_all_candidate()
    return render_template('candidate.html', records=results)

@candidate_blueprint.route('/upload_resumes')
def upload_resumes():
    return render_template('upload_resumes.html', uploaded=False)

@candidate_blueprint.route('/upload_bulk', methods=['POST'])
def upload_bulk():
    if 'files' not in request.files:
        return "No file part", 400
    
    files = request.files.getlist('files')

    for file in files:
        if file.filename: 
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            extracted_resume_text = extract_text_from_pdf(filepath)
            # print(extracted_resume_text)
            json_payload = parse_resume(extracted_resume_text)
            file.save(filepath)

            candidate_data = json.loads(json_payload)

            candidate_id = uuid.uuid4()
            candidate_dao = CandidateDAO()
            candidate_dao.insert_candidate_data(candidate_id, candidate_data)
            candidate_dao.insert_skills(candidate_id, candidate_data.get('skills', []))
            candidate_dao.insert_education(candidate_id, candidate_data.get('education', []))
            candidate_dao.insert_experience(candidate_id, candidate_data.get('experience', []))
            candidate_dao.insert_projects(candidate_id, candidate_data.get('projects', []))

    print("All data inserted successfully.")
    # return render_template('upload_resumes.html', uploaded=True)
    return f"{len(files)} file(s) uploaded successfully!"