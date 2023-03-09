from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta
import time

creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])

service = build('calendar', 'v3', credentials=creds)

for i in range(15):

    start = datetime.utcnow()
    start = start + timedelta(hours=-2, minutes=i)
    start = str(start).replace(' ', 'T')
    start = start.split('.')[0]
    print(start)
    start = str(start)

    end = datetime.utcnow()
    end = end + timedelta(hours=-1, minutes=i)
    end = str(end).replace(' ', 'T')
    end = end.split('.')[0]
    print(end)
    end = str(end)

    event = {
        'summary': 'OpenAI - Chat GPT overusage (5536.23$ unpaid invoice)',
        'location': 'Pioneer Building, San Francisco, California, US',
        'sendNotifications': True,
        'invitationMessage': 'Please join this meeting othwerwise we will contact authorities.',
        'sendUpdates': 'all',
        'sendNotifications': True,
        'guestsCanSeeOtherGuests': True,
        'guestsCanModify': True,
        'guestsCanInviteOthers': True,
        'sendNotifications': True,
        'reminders': {
            'useDefault': True,
        },
        'description': 'GPT overusage invoice',
        'start': {
            'dateTime': start,
            'timeZone': 'Europe/Warsaw',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Europe/Warsaw',
        },
        'attendees': [
            {'email': 'test.test@test.eu'}
           
        ]
    }

    event = service.events().insert(calendarId='primary', body=event, sendUpdates='all').execute()
    time.sleep(1)
