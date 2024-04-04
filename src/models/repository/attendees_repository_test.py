from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
db_connection_handler.connect_to_db()

def test_insert_attendee():
    event_id = "meu uid pae"
    attendees_info = {
        "uuid": "uuid do attendee",
        "name": "nome do attendee",
        "email": "emaildoattendee@gmail.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print (response)