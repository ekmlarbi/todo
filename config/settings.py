DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = '0.0.0.0:8080'
SECRET_KEY = 'insecurekeyfordev'

db_uri = 'postgresql://todo:devpassword@postgres:5432/todo'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
