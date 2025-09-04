from fastapi import FastAPI

from .routs import router as tasks_routing


app = FastAPI(
    openapi_url='/openapi.json',
    docs_url='/docs',
    debug=True)

app.include_router(tasks_routing)
