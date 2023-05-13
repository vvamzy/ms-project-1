import pyrebase

# Firebase configuration
config = {
    "apiKey": "apiKey",
    "authDomain": "projectId.firebaseapp.com",
    "databaseURL": "https://databaseName.firebaseio.com",
    "storageBucket": "bucket.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the database service
db = firebase.database()

# Query to fetch all the users
users = db.child("users").get()

# Print the users
for user in users.each():
    print(user.key(), user.val())
