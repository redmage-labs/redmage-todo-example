from redmage import Target

from todos import db

from ..jinja2_component import Jinja2Component


class TodoListComponent(Jinja2Component):
    template_path = "todos/components/todo_list_component/template.html"
    alias = "list"

    @Target.delete
    def delete_todo(self, todo_id: int):
        db.delete_todo(todo_id)
        return self.get_component("list")

    @Target.put
    def toggle(self, /, todo_id: int):
        todo = db.get_todo(todo_id)
        db.update_todo(todo.id, todo.message, not todo.finished)
        return self.get_component("list")
