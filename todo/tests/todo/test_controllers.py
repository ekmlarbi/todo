from flask import url_for


class TestTodo(object):

    def test_todo_home_page(self, client, todos):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('todo.home'))
        assert response.status_code == 200

