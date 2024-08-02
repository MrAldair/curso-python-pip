from fastapi import HTTPException
from src.lib.managedb import ManageDb

def put_contacts(id_contact, new_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.dict()
            
            if new_contact.name == "":
                contacts[index]["name"] = contact["name"]
                
            if new_contact.phone == "":
                contacts[index]["phone"] = contact["phone"]
                
            md.write_contacts(contacts)
            
            return {
                "Success": True,
                "message": "Contact Updated"
            }
    raise HTTPException(status_code=404, detail="Contact not Found")