#selenium for web driving
import selenium
from selenium import webdriver

# Time for pausing between navigation
import time

#Datetime for recording time of submission
import datetime

# os for file management

def submit():
    #Using Chrome to access web
    driver = webdriver.Chrome()

    time.sleep(5)

    #open the website
    driver.get("https://accounts.socialexplorer.com/login")

    #Locate log in with google button
    google_button = driver.find_element_by_link_text("Log in with Google")


if __name__ == "__main__":
    submit()