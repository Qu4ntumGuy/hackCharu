import firebase_admin

cred_obj = firebase_admin.credentials.Certificate()
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://jumping-fun-1fd86-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})