from redmage import Component
from redmage import elements as el
from starlette.responses import HTMLResponse


class TodoBaseComponent(Component):
    _redirect: str = None

    def __init__(self):
        self._redirect = None

    def set_redirect(self, path: str):
        self._redirect = path

    def build_response(self, content) -> HTMLResponse:
        if not self._redirect:
            return HTMLResponse(content)
        return HTMLResponse(
            status_code=302,
            headers={"HX-Redirect": self._redirect},
        )
