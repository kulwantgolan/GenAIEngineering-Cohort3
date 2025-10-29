# calculator.py
# A simple calculator with add and subtract functions
from fastapi import FastAPI  # ALternativvis - flask, django etc
import uvicorn  # to run the FastAPI app with Uvicorn server (Rest API server)

# Asynchronous Server Gateway Interface (ASGI) - Common ASGI web servers include Uvicorn, Hypercorn, and Daphne.
# ASGI (Asynchronous Server Gateway Interface) is the successor to WSGI (Web Server Gateway Interface) and provides a standardized way for Python applications to communicate with web servers.
# ASGI supports both synchronous and asynchronous applications, making it well-suited for modern web features like WebSockets, background tasks, and real-time event handling.

app = FastAPI()


# Shared function using FastAPI Endpoints
@app.get("/add")  # Define a GET endpoint at /add
def add(a, b):
    """Add two numbers and return the result."""
    result = float(a) + float(b)
    # result = a+b
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": result,
    }  # Return a JSON response with operation details


@app.get(
    "/subtract"
)  # Your FastAPI endpoint using @app.get("/subtract") works because, by default, query parameters in a GET request are mapped to the function arguments. This means you can call /subtract?a=7&b=2 and FastAPI will pass a and b to the subtract function as strings (which you then convert to float).
def subtract(a, b):
    """Subtract b from a and return the result."""
    result = float(a) - float(b)
    # result = a-b
    return {"operation": "subtract", "a": a, "b": b, "result": result}


@app.get("/")  # Define a root endpoint
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add or /subtract endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(
        app, host="0.0.0.0", port=9321
    )  # Run the FastAPI app with Uvicorn on port 9321

# http://localhost:9321/docs
# if changing program, restart the server

# Using github deploy to render.com - https://api-example-repeat.onrender.com/docs

"""
import requests
response = requests.get("http://localhost:9321/add", params={"a": 5, "b": 3})
print(response.json())
"""
