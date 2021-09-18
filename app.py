# imports
from flask import Flask
from flask_restful import Api
from resources.items import Items
import temp_db

# initialization

app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"] = True
api = Api(app)

# endpoints
api.add_resource(Items, "/items")

# database initialization
temp_db.create_table()
if not temp_db.check_records():
    temp_db.insert_into_table()

temp_db.show_all()

# execution
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
