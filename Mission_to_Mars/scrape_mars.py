#Dependencies 

import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser

def init_browswer():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return browser = Browser('chrome', **executable_path, headless=False)

mars_dict = {}

def mars_news():
    browser = init_browser()

    #visit the Mars News URL

    url = 'https://mars.nasa.gov/news/'
    browswer.visit(url)

    # Parsing HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #latest headline and blurb
    news_title = soup.find('div', class_='content_title').find('a').text.strip()
    p_news = soup.find('div', class_='rollover_description_inner').text.strip()
    
    #add them to the dict

    mars_dict["News_Title"] = news_title
    mars_dict["News_Paragraph"] = p_news
    
    return mars_info
    
    browser.quit()


