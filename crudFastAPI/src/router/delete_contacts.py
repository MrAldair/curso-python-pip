from fastapi import HTTPException

from src.lib.managedb import ManageDb

def delete_contacts(id_contact):
    md = ManageDb()
    contacts = md.read_contacts()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)
            
            md.write_contacts(contacts)
            
            return{
                "success": True, 
                "message": "Contact Deleted"
            }
            
    raise HTTPException(status_code=404, detail="Contact not Found")