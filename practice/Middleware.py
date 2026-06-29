from fastapi import FastAPI, Request,HTTPException
import time
 
app = FastAPI()


@app.middleware("http")
async def log_middle(request:Request, call_next):
    start_line = time.time()

    response = await call_next(Request)

    process_time = time.time() - start_line

    print(f"Path:{request.url.path} | Time:{process_time}")

    print(f"Status :{response.status_code}")

    return response




# @app.middleware("http")
# async def my_middleware(request:Request , call_next):
#     print("Request Recieved")

#     response = await call_next(request)

#     print("Response Sent")

#     return response