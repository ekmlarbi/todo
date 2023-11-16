from flask import Blueprint, render_template, flash, redirect, url_for
from todo.blueprints.todo.forms import TodoForm
from todo.blueprints.todo.models import Todo

todo = Blueprint('todo', __name__, template_folder='templates')


@todo.route('/', methods=['GET', 'POST'])
def home():
    form = TodoForm()

    if form.validate_on_submit():
        o = Todo()
        form.populate_obj(o)
        if o.save():
            flash("Todo saved successfully", 'success')
            return redirect(url_for('todo.home'))

    todo_list = Todo.query.all()  # best to paginate
    return render_template('todo/home.html', form=form, todo_list=todo_list)


@todo.route('/todo/update/<int:todo_id>', methods=['GET'])
def update(todo_id):
    o = Todo.query.get(todo_id)
    if o:
        o.status = not o.status
        o.save()
        flash("Updated todo successfully", 'info')
        return redirect(url_for("todo.home"))


@todo.route('/todo/delete/<int:todo_id>', methods=['GET'])
def delete(todo_id):
    o = Todo.query.get(todo_id)
    if o:
        s = o.name
        o.delete()
        flash(f"Deleted todo '{s}'", 'danger')
        return redirect(url_for("todo.home"))
