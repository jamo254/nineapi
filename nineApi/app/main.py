from fastapi import FastAPI
from nineApi.app.routers import user

app = FastAPI()

app.include_router(user.router)

# Settting up server
if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)