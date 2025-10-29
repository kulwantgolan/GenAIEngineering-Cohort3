from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

"""
Cross origin communicaiton: Cross-origin communication happens when a web page loaded from one origin (domain, protocol, port) tries to interact with a server at a different origin. 
e.g. JavaScript code running on a frontend (e.g., at http://localhost:3000) to interact with a backend API hosted at a different origin (e.g., http://localhost:8000).
By default, browsers restrict such cross-origin communication due to security policies (same-origin policy). 

How CORS works:
When a browser sees that your script is making a cross-origin request, it automatically adds special headers like Origin.
If the target server wants to allow this, it explicitly responds with headers such as Access-Control-Allow-Origin, listing the origins permitted to access its resources.​
If the right CORS headers are missing, the browser blocks the response even if the server sends data

CORSMiddleware - Adds the necessary CORS headers (Access-Control-Allow-Origin and others) to your HTTP responses. to allow cross-origin requests.
Needed for public APIs accessed from web frontends hosted on different domains.
"""

"""
FAST API  running on different server - render.com (Backend) : FastAPI backend must explicitly allow requests coming from the Streamlit app’s origin by enabling CORS.
Applicaiton Frontend is running on different server -  streamlit (frontend)
Got difeerent origin (https/http + domain + port)

"""


# Create FastAPI instance with metadata for documentation
app = FastAPI(
    title="text API", description="A simple text API with processing", version="0.2.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict this in production
    allow_credentials=True,  # if cred like cookies, auth headers needed, allow origin must be explicit and not "*"
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define Pydantic models for request validation
class TextInput(BaseModel):
    a: str = Field(..., description="Lengthy String")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "a": "Any lenghy string that spans more number of words",
                }
            ]
        }
    }


@app.post("/count")
def add(text: TextInput):
    """Add two numbers and return the result."""
    result = len(text.a.split())
    return {f"length of string: {result} words"}


@app.post("/split")
def subtract(text: TextInput):
    """Subtract b from a and return the result."""
    result = text.a.split()
    return result


@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add or /subtract endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9321)
