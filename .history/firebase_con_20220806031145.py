import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\Users\Gaurav\Downloads\jumping-fun-1fd86-firebase-adminsdk-vetn9-7f4b11a4e8.json")
firebase_admin.initialize_app(cred)
