from lib.util_sqlalchemy import ResourceMixin
from todo.extensions import db


class Todo(ResourceMixin, db.Model):
    #__tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column('status', db.Boolean(), nullable=False, server_default='0')
    name = db.Column(db.String(255), index=True, nullable=False, server_default='')

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(Todo, self).__init__(**kwargs)
