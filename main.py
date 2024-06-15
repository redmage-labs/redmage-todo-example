import logging

# setup logging before importing app
logging.basicConfig()
logging.getLogger("redmage").setLevel(logging.DEBUG)

import uvicorn

from todos import app

if __name__ == "__main__":
    uvicorn.run(app.starlette, host="0.0.0.0", port=8000)
