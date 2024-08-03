from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4 as uuid
from pydantic import BaseModel


from src.router.get_contacts import get_contacts
from src.router.get_contact import get_contact
from src.router.post_contacts import post_contacts
from src.router.put_contacts import put_contacts
from src.router.delete_contacts import delete_contacts

class ContactModel(BaseModel):
    id: str = str(uuid())
    name: str
    phone: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="./public/static"), name="static")

templates = Jinja2Templates(directory="./public/templates")

@app.get('/', response_class=HTMLResponse)
def root():
    html_address = "./public/static/html/index.html"
    return FileResponse(html_address, status_code=200)

@app.get("/api/contacts", response_class=HTMLResponse)
def get_all_contacts(request: Request):
    contacts = get_contacts()
    return templates.TemplateResponse("contacts.html", {"request":request, "contacts": contacts}, status_code=200)

#Trabajando aqui
#@app.get("/api/contacts/{id_contact}", response_class="HTMLResponse")
#def get_single_contact(request: Request, id_contact:str):
#    return get_contact(id_contact)
    #return templates.TemplateResponse("item.html",{"request": request, "id_contact": id_contact})

@app.get("/api/contacts/{id_contact}", response_class=HTMLResponse)
def get_single_contact(request: Request, id_contact: str):
    contact = get_contact(id_contact)
    return templates.TemplateResponse("item.html", {"request": request, "contact": contact})



@app.post("/api/contacts")
def add_contact(new_contact: ContactModel):
    return post_contacts(new_contact)
    
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact:str, new_contact: ContactModel):
    return put_contacts(id_contact, new_contact)

@app.delete('/api/contact/{id_contact}')
def remove_contact(id_contact:str):
    return delete_contacts(id_contact)