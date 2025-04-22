from fastapi import FastAPI
import uvicorn
import json


# working fastapi
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)  # 8000
