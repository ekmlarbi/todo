from todo.blueprints.todo.models import Todo


class TestTodo(object):
    def test_todos_list(self, todos):
        lst = Todo.query.all()
        assert len(lst) == 2

    def test_todo_create(self, session):
        todo = Todo(name='Sample Todo Test', status=False)
        session.add(todo)
        session.commit()

        lst = Todo.query.all()
        assert len(lst) == 3
