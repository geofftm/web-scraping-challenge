from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

import scrape_mars

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# # Connect to a database. Will create one if not already available.
db = client.mars_db

# @app.route("/")
# def index():
#     mars_info = mongo.db.mars_db.find_one()
#     return render_template("index.html", data=mars_info)




# @app.route('/scrape')
# def scrape():
   


if __name__ == "__main__":
    app.run(debug=True)