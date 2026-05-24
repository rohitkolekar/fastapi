
## Steps Planned

1. Create basic fastAPI app 
2. Publish Local 
3. Verify 
4. Publish to render 
5. Publish on azure 
6. Document all steps 


## Step 1 Create virtual environment using command prompt and activate 
python -m venv .venv

.venv\Scripts\activate.bat

pip list

## Step 2 Install Libraries 

pip install fastapi

pip install uvicorn["standard"]

pip list 


## Step 3 Open the root folder in VS code and add new file 

file added and named books.py 

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI"
    }

@app.get("/endpoint")
def endpoint():
    return {
        "message": "Endpoint from FastAPI"
    }

```

## Step 4 Run the application 

 uvicorn books:app --reload

 <!--
books is the file name 
app is the FastAPI object
-->

## Step 5 Verify 
http://127.0.0.1:8000/


## Step 6 Use swagger to view and test all API
http://127.0.0.1:8000/docs

## Step 8 Publish to Github
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/rohitkolekar/fastapi.git
git push -u origin master

## Step 9 publish on render 
