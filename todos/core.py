from redmage import Redmage
from starlette.convertors import register_url_convertor
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from .router import RouteConvertor

register_url_convertor("Route", RouteConvertor())

app = Redmage()

app.routes.append(
    Mount(
        "/static",
        app=StaticFiles(directory="./todos/static"),
        name="static",
    )
)

# Have to register the convertors before importing the components
# Only need to import the top level component so everything else is imported
from .components.todo_app_component import TodoAppComponent
