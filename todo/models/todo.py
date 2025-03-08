import datetime
from . import db

class Todo(db.Model):
    __tablename__ = 'todos'
    # This is how to define a column. This is also the primary key,
    id = db.Column(db.Integer, primary_key=True)
    # This is a mandatory column of 80 chars.
    title = db.Column(db.String(80), nullable=False)
    # This is an optional column of 120 chars.
    description = db.Column(db.String (120), nullable=True)
    # Column with default value of false.
    completed = db.Column(db.Boolean, nullable=False, default=False)
    # Column with a DateTime value.
    deadline_at = db.Column(db.DateTime, nullable=True)
    # Colum has a default value which is a function call (this means it is inserted when the record is created).
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    # Colum updates on update.
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    
    # Helper method ot convert the model to a dictionary. This allows lookups by a key value (get()).
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'deadline_at': self.deadline_at.isoformat() if self.deadline_at else None,
            'created_at': self.created_at.isoformat() if self.deadline_at else None,
            'updated_at': self.updated_at.isoformat() if self.deadline_at else None,
        }
    
    def __repr__(self):
        return f'<Todo {self.id} {self.title}>'
    