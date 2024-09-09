from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# Dummy api Key
API_KEY = '12345-ABCDE-67890-FGHIJ'
# Initialize the app
app = FastAPI()
# Get the templates
templates = Jinja2Templates(directory="app/templates")
#get request to get the HTML template
@app.get("/contador", response_class=HTMLResponse)
def contador(request:Request):
    return templates.TemplateResponse(request=request, name="index.html")
