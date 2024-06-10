from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from . import smokeTest
from fastapi_gcs import FGCSUpload

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


@app.post("/upload-file/")
async def create_upload_file(file: UploadFile):
    return await FGCSUpload.file(
    	project_id='invima-424416', 
        bucket_name='invima-bucket-staging', 
        file=file, 
        file_path='my_data/test', 
        maximum_size=2_097_152, 
        allowed_extension= ['pdf'],
        #file_name='my_file.png' #optional custom file name
    )
    
    