import pytest
from todo.app import create_app
from config import settings
from todo.extensions import db as _db
from todo.blueprints.todo.models import Todo


@pytest.fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    db_uri = '{0}_test'.format(settings.SQLALCHEMY_DATABASE_URI)
    params = {
        'DEBUG': False,
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
        'SQLALCHEMY_DATABASE_URI': "sqlite://"
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()


@pytest.fixture(scope='session')
def db(app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: SQLAlchemy database session
    """
    _db.drop_all()
    _db.create_all()

    params = {
        'name': 'Sample Todo',
        'status': False,
    }
    todo = Todo(**params)
    _db.session.add(todo)
    _db.session.commit()

    return _db


@pytest.fixture(scope='function')
def session(db):
    """
    Allow very fast tests by using rollbacks and nested sessions. This does
    require that your database supports SQL savepoints, and Postgres, SQLite do.

    Read more about this at:
    http://stackoverflow.com/a/26624146

    :param db: Pytest fixture
    :return: None
    """
    db.session.begin_nested()

    yield db.session

    db.session.rollback()


@pytest.fixture(scope='function')
def todos(db):
    """
    Create todo fixtures. They reset per test.

    :param db: Pytest fixture
    :return: SQLAlchemy database session
    """
    db.session.query(Todo).delete()

    todos = [
        {
            'name': 'Sample Todo 1',
            'status': False,
        },
        {
            'name': 'Sample Todo 2',
            'status': True,
        }
    ]

    for todo in todos:
        db.session.add(Todo(**todo))

    db.session.commit()

    return db
