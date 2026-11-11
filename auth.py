from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = [
'https://www.googleapis.com/auth/drive.file'
]
file_name = 'client_secret_744285131798-2m5n0b6ndqtsjvmpluerdpgm2ab0949j.apps.googleusercontent.com.json'
path = Path.home() / 'Downloads'/ file_name
flow = InstalledAppFlow.from_client_secrets_file(str(path), scopes)