from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees

class AttendeesRepository:
    def insert_attendee(self, attendee_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                atendee = (
                    Attendees(
                        id = attendee_info.get("uuid"),
                        name = attendee_info.get("name"),
                        email = attendee_info.get("email"),
                        event_id = attendee_info.get("event_id")
                    )
                )
                database.session.add(atendee)
                database.session.commit()

                return attendee_info
            except Exception as exeption:
                database.session.rollback()
                raise exeption