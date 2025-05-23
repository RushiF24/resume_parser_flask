from base import db_client

class CandidateDAO():
    def get_all_candidate(self):
        query = 'SELECT * from candidate'
        results = db_client.execute(query)

        return results

    def insert_candidate_data(self, candidate_id, candidate):
        print('Inserting candidate')
        sql = "INSERT INTO candidate (id, name, email, phone) VALUES"
        data = [(
            candidate_id,
            candidate.get('name', '') or '',
            candidate.get('email', '') or '',
            candidate.get('phone', '') or ''
        )]
        db_client.execute(sql, data)
    
    def insert_skills(self, candidate_id, skills):
        print('Inserting skills')
        skills = skills or []
        sql = "INSERT INTO skills (candidate_id, skill) VALUES"
        data = [(candidate_id, skill) for skill in skills if skill]
        if data:
            db_client.execute(sql, data)
        
    def insert_education(self, candidate_id, education_list):
        print('Inserting education')
        education_list = education_list or []
        sql = """
            INSERT INTO education (candidate_id, degree, institution, start_date, end_date, cgpa, percentage) 
            VALUES
        """
        data = [(
            candidate_id,
            edu.get('degree', '') or '',
            edu.get('institution', '') or '',
            edu.get('start_date', '') or '',
            edu.get('end_date', '') or '',
            edu.get('cgpa', '') or '',
            edu.get('percentage', '') or ''
        ) for edu in education_list]
        if data:
            db_client.execute(sql, data)
    
    
    def insert_experience(self, candidate_id, experience_list):
        print('Inserting experience')
        experience_list = experience_list or []
        sql = "INSERT INTO experience (candidate_id, title, company, start_date, end_date) VALUES"
        data = [(
            candidate_id,
            exp.get('title', '') or '',
            exp.get('company', '') or '',
            exp.get('start_date', '') or '',
            exp.get('end_date', '') or ''
        ) for exp in experience_list]
        if data:
            db_client.execute(sql, data)

    def insert_projects(self, candidate_id, project_list):
        print('Inserting projects')
        project_list = project_list or []
        sql = """
            INSERT INTO projects (candidate_id, title, description, github_link, start_date, end_date) 
            VALUES
        """
        data = [(
            candidate_id,
            proj.get('title', '') or '',
            proj.get('description', '') or '',
            proj.get('github_link', '') or '',
            proj.get('start_date', '') or '',
            proj.get('end_date', '') or ''
        ) for proj in project_list]
        if data:
            db_client.execute(sql, data)