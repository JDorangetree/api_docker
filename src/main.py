from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest

#import debugpy

#debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(smokeTest.router, prefix="/smoke-test")

# Define the API endpoints
@app.get('/')
def health():
    return {
        "message": "OK CICD"
    }


@app.post("/file/upload")
def upload_file(file: UploadFile):
    return {"filename": file.filename}