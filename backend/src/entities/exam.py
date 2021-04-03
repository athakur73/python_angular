from sqlalchemy import Column, String
from marshmallow import Schema, fields
from .entity import Entity, Base
from sqlalchemy.ext.serializer import loads, dumps

class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String)
    description = Column(String)

    #serialize_only = ('id', 'email_id', 'role_type', 'users.id')
    _default_fields = [
        "title",
        "description",
    ]
    _hidden_fields = []
    _readonly_fields = []

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
    
    
    

class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()

