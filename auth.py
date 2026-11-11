from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import os
from dotenv import load_dotenv

def get_credentials():
    scopes = [
    'https://www.googleapis.com/auth/drive.file'
    ]

    path = Path("client_secret.json")
    creds = None
    token = 'token.json'
    if Path(token).is_file():
        creds = Credentials.from_authorized_user_file(token, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else: 
            flow = InstalledAppFlow.from_client_secrets_file(str(path), scopes)
            creds = flow.run_local_server(port=0)
        Path(token).write_text(creds.to_json())
    print("Авторизация успешна:", creds.valid)
    return creds

def work_with_sheets(creds):
    service = build('sheets', 'v4', credentials=creds)


work_with_sheets(get_credentials())
print(dir(os.environ))