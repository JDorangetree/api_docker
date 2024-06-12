from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest
from fastapi_gcs import FGCSUpload


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
        "message": "OK CICD nuevo"
    }


@app.post("/upload-file/")
async def create_upload_file(file: UploadFile):
    return await FGCSUpload.file(
    	project_id='dockerapi-425716', 
        bucket_name='documents_staging', 
        file=file, 
        file_path='../', 
        maximum_size=2_097_152, 
        allowed_extension= ['pdf'],
        #file_name='my_file.png' #optional custom file name
    )
    
    