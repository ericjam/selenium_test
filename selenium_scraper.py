from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from pyvirtualdisplay import Display
from urllib.error import URLError
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import time
import random
from bs4 import BeautifulSoup
import bs4
import os
import sys

with Display():

    delay = 3
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    
    try:

        # driver.get('https://www.nadaguides.com/Boats/2017/Grady-White-Boats/180-FISHERMAN-CC_/32072308/Specs')
        # driver.get('https://www.nadaguides.com/Boats/2017/Grady-White-Boats')
        driver.get('https://www.boattrader.com/browse/pleasure-boats/florida/')
    
        boat_list = driver.find_element_by_class_name('browse-listings-photo')

        for i in boat_list.find_elements_by_css_selector('a'):
            print(i.text)


        # engine_manufacturer = driver.find_element_by_xpath("//*[contains(text(), 'Engine Manufacturer')]")
        # engine_parent = engine_manufacturer.find_element_by_xpath('..')
        # print(engine_parent.text)

    finally:
        driver.quit()

