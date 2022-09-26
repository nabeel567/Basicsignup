import pymongo
client = pymongo.MongoClient("mongodb+srv://nabeelabrar12796:PFRE938wbg8lStPc@cluster0.nybmfwj.mongodb.net/?retryWrites=true&w=majority")

FLASK_APP_DB = client.flask_app
