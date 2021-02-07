# from flask import Flask, render_template

# # Import our pymongo library, which lets us connect our Flask app to our Mongo database.
# import pymongo

# import scrape_mars

# # Create an instance of our Flask app.
# app = Flask(__name__)

# # Create connection variable
# conn = 'mongodb://localhost:27017/mars_db'

# # # Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# # # # Connect to a database. Will create one if not already available.
# db = client.mars_db

# @app.route("/")
# def index():
#     mars_info = client.db.mars_dict.find_one()
#     return render_template("index.html", data=mars_info)




# @app.route('/scrape')
# def scrape():
#     mars_news = scrape_mars.mars_news()
#     mars_imgs = scrape_mars.mars_featured_img()
#     mars_facts = scrape_mars.mars_facts()
#     mars_hemis = scrape_mars.mars_hemispheres()
#     db.update({}, mars_news, upsert=True)

#     return redirect("/", code=302)

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_news.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    news = mongo.db.mars_news
    # Run the scrape function
    mars_facts = scrape_mars.mars_facts()
    mars_news = scrape_mars.mars_news()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_news.update({}, mars_news, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


   
