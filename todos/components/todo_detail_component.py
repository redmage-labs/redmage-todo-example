from redmage import Target
from redmage import elements as el

from todos.components.todo_base_component import TodoBaseComponent

from ..db import Todo, get_todo, update_todo


class TodoDetailComponent(
    TodoBaseComponent,
):
    def __init__(self, todo_id: str):
        self.todo_id = int(todo_id)
        super().__init__()

    async def render(self):
        try:
            todo = get_todo(self.todo_id)
        except Exception as err:
            print(err)
            return el.Div("Todo not found")

        return el.Div(
            el.Form(
                el.Label(
                    "Message",
                    el.Textarea(
                        todo.message,
                        type="text",
                        name="message",
                        required=True,
                        rows=5,
                        cols=80,
                    ),
                ),
                el.Label(
                    "Finished",
                    el.Input(
                        type="checkbox",
                        name="finished",
                        checked=todo.finished,
                    ),
                ),
                el.Button(
                    "Save",
                    type="submit",
                    click=self.update_todo(self.todo_id),
                ),
                _class="table rows",
            ),
        )

    @Target.put
    def update_todo(self, todo: Todo, /, todo_id: int):
        self.todo_id = todo_id
        update_todo(todo_id, todo.message, todo.finished)
        self.set_redirect("/")
