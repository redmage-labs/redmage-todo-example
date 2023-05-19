from redmage import Target

from ... import db
from ..jinja2_component import Jinja2Component


class TodoEditComponent(Jinja2Component):
    template_path = "todos/components/todo_edit_component/template.html"
    alias = "edit"

    def __init__(self, todo_id: int):
        self.todo_id = todo_id

    @property
    def todo(self):
        if not hasattr(self, "_todo"):
            self._todo = db.get_todo(self.todo_id)
        return self._todo

    @Target.put
    def edit_todo(self, todo: db.Todo, /, todo_id: int):
        self.todo_id = todo_id
        db.update_todo(todo_id, todo.message, self.todo.finished)
        return self.get_component("list")
