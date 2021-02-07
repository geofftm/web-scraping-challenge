#Dependencies 

import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

mars_dict = {}

def mars_news():
    #browser = init_browser()

    #visit the Mars News URL

    url = 'https://mars.nasa.gov/news/'
    #browswer.visit(url)

    # Parsing HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #latest headline and blurb
    news_title = soup.find('div', class_='content_title').find('a').text.strip()
    p_news = soup.find('div', class_='rollover_description_inner').text.strip()
    
    #add them to the dict

    mars_dict["News_Title"] = news_title
    mars_dict["News_Paragraph"] = p_news
    
    return mars_dict
    
    #browser.quit()

def mars_featured_img():

    browser = init_browser()

    featured_img_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    #Visit the site with the featured image
    browser.visit(featured_img_url)
    #html object
    html = browser.html
    # parsing the html
    soup = BeautifulSoup(html, 'html.parser')
    #search for the image link
    featured_image = soup.find('a', class_='showimg fancybox-thumbs')
    href = featured_image['href']
    #setting base url by replacing index.html
    img_url = featured_img_url.replace('index.html', '')
    #concatenate the strings to make final url
    final_img_url = img_url + href

    mars_dict["Featured_URL"] = final_img_url

    browser.quit()

    return mars_dict

def mars_facts():
    
    #mars facts url

    facts_url = 'https://space-facts.com/mars/'
    response = requests.get(facts_url)
    soup = BeautifulSoup(response.text)

    #Parse HTML using Pandas
    tables = pd.read_html(facts_url)
    df = tables[0]
    html_table = df.to_html()

    mars_dict['tables'] = html_table
    
    return mars_dict


def mars_hemispheres():
    
    browser = init_browser()
    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    aitems = soup.find_all('div', class_='item')
    base_url = hemis_url.replace('/search/results?q=hemisphere+enhanced&k1=target&v1=Mars', '')
    hemisphere_image_urls = []
    
    for item in aitems:
        #find the title by going to the h3 tag
        title = item.find('h3').text
        #find the img ref in the href tag of an a tag with with itemLinkClass
        part_img_ref = item.find('a', class_='itemLink product-item')['href']
        #concantenate the base url with the part_img_ref and visit that new url
        browser.visit(base_url+part_img_ref)
        #html object of new page
        partial_img_html = browser.html
        #parsing html of new page
        soup = BeautifulSoup(partial_img_html, 'html.parser')
        #grabbing the full image path from the img tag/source attribute and concatenating with base url
        img_url = base_url+soup.find('img', class_='wide-image')['src']
        #appending final concatenated urls into the empty list in dict format
        hemisphere_image_urls.append({"Title": title, "img_url": img_url})


    mars_dict["Mars_Hemisphere_Image_URLS"] = hemisphere_image_urls

    browser.quit()

    return mars_dict

if __name__ == "__main__":
    mars_news()
    mars_featured_img()
    mars_facts()
    mars_hemispheres()


    


    
    




