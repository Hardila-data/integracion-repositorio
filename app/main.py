from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# Dummy api Key
api_key_example = "ghp_1234567890abcdefghijklmnopqrstuvwxyz1234"
# Initialize the app
app = FastAPI()
# Get the templates
templates = Jinja2Templates(directory="app/templates")
#get request to get the HTML template
@app.get("/contador", response_class=HTMLResponse)
def contador(request:Request):
    return templates.TemplateResponse(request=request, name="index.html")
