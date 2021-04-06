#from .entities.entity import Session, engine, Base

# sources
#https://medium.com/@anushkamehra16/connecting-to-sql-database-using-sqlalchemy-in-python-2be2cf883f85
#https://medium.com/@alanhamlett/part-1-sqlalchemy-models-to-json-de398bc2ef47#:~:text=To%20add%20a%20serialization%20method,columns%20and%20returns%20a%20dictionary.&text=def%20to_dict(self%2C%20show%3D,of%20this%20model.%22%22%22
#sources

#from entities.exam import Exam,ExamSchema
from entities.database import employee,project
from entities.database import Session, engine, Base
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import time
import datetime
app = Flask(__name__)
CORS(app)
from sqlalchemy.ext.serializer import loads, dumps

# generate database schema
Base.metadata.create_all(engine)

# start session
# session = Session()

# check for existing data
# exams = session.query(Exam).all()
# if len(exams) == 0:
#     # create and persist mock exam
#     python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
#     session.add(python_exam)
#     session.commit()
#     session.close()

#     # reload exams
#     exams = session.query(Exam).all()

# show existing exams
# print('### Exams:')
# for exam in exams:
#     print(f'({exam.id}) {exam.title} - {exam.description}')

@app.route('/employees')
def employees():
    session = Session()
    emp_objects = session.query(employee).all()
    serialized_obj = [{"title":obj.title,"description":obj.description} for obj in emp_objects]
    session.close()
    return (jsonify(serialized_obj))

@app.route('/projects')
def projects():
    session = Session()
    project_objects = session.query(project).all()
    serialized_obj = [{"title":obj.title,"description":obj.description} for obj in project_objects]
    session.close()
    return (jsonify(serialized_obj))

@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    data = request.get_json()
    emp_data = employee(first_name=data["first_name"] , 
                        last_name = data["last_name"], 
                        sur_name= data["sur_name"], 
                        initial= data["initial"], 
                        salutation= data["salutation"], 
                        project_id= data["project_id"], 
                        dept= data["dept"], 

                        emp_start_date= datetime.datetime(),
                        emp_last_working_date=datetime.datetime(),
                        emp_project_assigned_date=datetime.datetime(),
                        emp_project_end_date=datetime.datetime(),

                        employment_status=data["employment_status"], 
                        manager_name=data["manager_name"], 
                        manager_dept=data["manager_dept"], 

                        )
    session = Session()
    session.add(emp_data)
    session.commit()
    emp_data.to_dict()
    return jsonify(emp_data.to_dict()), 201


@app.route('/addProject', methods=['POST'])
def addProject():
    data = request.get_json()
    project_data = project(project_id=data["project_id"] , 
                        project_title = data["project_title"], 
                        project_start_date= datetime.datetime.now(),
                        project_status= data["status"], 
                        
                        )
    session = Session()
    session.add(project_data)
    session.commit()
    project_data.to_dict()
    return jsonify(project_data.to_dict()), 201

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000,debug = True)