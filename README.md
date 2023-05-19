# redmage-todo-example

An example todo application using redmage + htmx.

This example was created to demonstrate how you can organize your app by using a single file for each component and Jinja2 as a template engine.

## Dependencies

### Javascript

* [https://github.com/bigskysoftware/htmx](htmx) (via CDN)

### Python
* [https://github.com/pallets/jinja](jinja2)
* [https://github.com/redmage-labs/redmage](redmage)
* [https://github.com/encode/uvicorn](uvicorn)

### CSS and icons
* [https://github.com/feathericons/feather](feathericons)
* [https://github.com/picocss/pico](pico.css) (via CDN)

## Run the app

This app has only been tested on Python 3.10 and uses poetry to manage dependencies.


### Install dependencies

```
poetry install
```

### Run the Todo app

```
poetry run python main.py
```

The todo app will be available at port [http://localhost:8000/]