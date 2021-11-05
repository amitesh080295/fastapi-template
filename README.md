# fastapi-template
Python REST API development template based on the FastAPI framework. The code follows the objected oriented design pattern and dependency injection helps loading the components as required. The application runs on the Uvicorn ASGI Web Server.

# Running Locally
**Prerequisites**
- Python >=3.7

```
#Install dependencies from requirements.txt
pip install -r requirements.txt

# Run the application
uvicorn src.app:app
```

In your browser, go to http://127.0.0.1:8000/api/v1/sample_endpoint. You should see the following output
`{"message":"Success"}`

