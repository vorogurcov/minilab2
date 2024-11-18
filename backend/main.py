import sys
import os
import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend import routers
from backend.config import settings


from fastapi.responses import JSONResponse

# Добавление пути к папке backend в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

if len(settings.CORS_ORIGINS) > 0:
    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
                       allow_methods=['*'], allow_headers=['*'])
routers.init_app(app)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=settings.PORT, reload=True)
