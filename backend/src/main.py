#from .entities.entity import Session, engine, Base

# sources
#https://medium.com/@anushkamehra16/connecting-to-sql-database-using-sqlalchemy-in-python-2be2cf883f85
#https://medium.com/@alanhamlett/part-1-sqlalchemy-models-to-json-de398bc2ef47#:~:text=To%20add%20a%20serialization%20method,columns%20and%20returns%20a%20dictionary.&text=def%20to_dict(self%2C%20show%3D,of%20this%20model.%22%22%22
#sources
from entities.exam import Exam,ExamSchema
from entities.entity import Session, engine, Base
from flask import Flask, jsonify, request
app = Flask(__name__)
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

@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()
    serialized_obj = [{"title":obj.title,"description":obj.description} for obj in exam_objects]
    session.close()
    return (jsonify(serialized_obj))


@app.route('/exams', methods=['POST'])
def add_exam():
    data = request.get_json()
    posted_exam = Exam(title=data["title"] , description = data["description"], created_by= "Post request")
    session = Session()
    session.add(posted_exam)
    session.commit()
    posted_exam.to_dict()
    return jsonify(posted_exam.to_dict()), 201

if __name__ == '__main__':
    app.run(debug = True)