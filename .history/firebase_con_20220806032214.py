import firebase_admin

cred_obj = firebase_admin.credentials.Certificate('C:\Users\Gaurav\Downloads\jumping-fun-1fd86-firebase-adminsdk-vetn9-7f4b11a4e8.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://jumping-fun-1fd86-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})