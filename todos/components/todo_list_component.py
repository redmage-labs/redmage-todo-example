from redmage import Target
from redmage import elements as el

from todos.components.todo_base_component import TodoBaseComponent

from ..db import Todo, create_todo, delete_todo, get_todo, get_todos, update_todo


class TodoListComponent(
    TodoBaseComponent,
):
    async def render(self):
        todos: list[Todo] = get_todos()
        return el.Div(
            el.P("No todos yet!")
            if not todos
            else el.Ul(
                *[
                    el.Li(
                        el.A(
                            el.S(todo.message) if todo.finished else todo.message,
                            href=f"/todo/{todo.id}",
                        ),
                        el.Button(
                            "Finish",
                            click=self.toggle_todo(todo.id),
                        ),
                        el.Button(
                            "Delete",
                            click=self.delete_todo(todo.id),
                        ),
                    )
                    for todo in todos
                ]
            ),
            el.Button("Create Todo", click=self.create_todo()),
        )

    @Target.post
    async def create_todo(self):
        todo = create_todo("", False)
        self.set_redirect(f"/todo/{todo.id}")

    @Target.delete
    async def delete_todo(self, todo_id: int):
        delete_todo(todo_id)

    @Target.put
    async def toggle_todo(self, todo_id: int):
        todo = get_todo(todo_id)
        update_todo(todo_id, todo.message, not todo.finished)
