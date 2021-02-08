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
    mars_image = mongo.db.mars_img.find_one()
    mars_facts = mongo.db.mars_facts.find_one()
    mars_hemis = mongo.db.mars_hemis.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data, mars_image=mars_image, mars_facts=mars_facts, mars_hemis=mars_hemis)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # news = mongo.db.mars_news
    # Run the scrape function
    mars_facts = scrape_mars.mars_facts()
    mars_news = scrape_mars.mars_news()
    mars_img = scrape_mars.mars_featured_img()
    mars_hemis = scrape_mars.mars_hemispheres()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_news.update({}, mars_news, upsert=True)
    mongo.db.mars_img.update({}, mars_img, upsert=True)
    mongo.db.mars_facts.update({}, mars_facts, upsert=True)
    mongo.db.mars_hemis.update({}, mars_hemis, upsert=True)
    


    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)


   
