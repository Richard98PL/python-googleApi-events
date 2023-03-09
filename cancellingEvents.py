from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta

creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])

service = build('calendar', 'v3', credentials=creds)

calendar_id = 'primary'

# Get all events from the primary calendar
now = datetime.utcnow()
now = now + timedelta(days=7)
maxTime = now.isoformat() + 'Z'  # 'Z' indicates UTC time

now = now + timedelta(days=-14)
minTime = now.isoformat() + 'Z'  # 'Z' indicates UTC time

print(maxTime)
print(minTime)

events_result = service.events().list(calendarId=calendar_id, 
                                      timeMax=maxTime,
                                      timeMin=minTime,
                                      maxResults=2500, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])
#print(events)

# Delete all events
all = True
for event in events:
    if all is True:
        #service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()

        service.events().delete(
        calendarId='primary', # Replace with your own calendar ID
        eventId=event['id']).execute()
    else:
        if 'start' in event and 'dateTime' in event['start']:
            dateStart = str(event['start']['dateTime']).split('T')[0]
            if dateStart == '2023-03-09':
                print(event['summary'])
                if event['summary'] == 'test':
                    service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()
