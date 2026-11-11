from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

scopes = [
'https://www.googleapis.com/auth/drive.file'
]
# file_name = 'client_secret_744285131798-2m5n0b6ndqtsjvmpluerdpgm2ab0949j.apps.googleusercontent.com.json'
# path = Path.home() / 'Downloads'/ file_name
# flow = InstalledAppFlow.from_client_secrets_file(str(path), scopes)
# creds = flow.run_local_server(port=0)
# print("Авторизация успешна:", creds.valid)


creds = None
token = 'token.json'
if Path(token).is_file():
    creds = Credentials.from_authorized_user_file(token, scopes)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        request = google.auth.transport.requests.Request()
        creds.refresh(request)
service = build('sheets', 'v4', credentials=creds)
