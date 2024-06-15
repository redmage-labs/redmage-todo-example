# redmage-todo-example

An example todo application using redmage + htmx.

## Dependencies

### Javascript

* [https://github.com/bigskysoftware/htmx](htmx) (via CDN)

### Python
* [https://github.com/redmage-labs/redmage](redmage)
* [https://github.com/encode/uvicorn](uvicorn)

### CSS and icons
* [https://missing.style/](missing.css) (via CDN)

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