from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = [
'https://www.googleapis.com/auth/drive.file'
]

path = Path.home() / 'client_secret_744285131798-2m5n0b6ndqtsjvmpluerdpgm2ab0949j.apps.googleusercontent.com'
