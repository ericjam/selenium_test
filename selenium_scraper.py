from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from urllib.error import URLError
# from selenium.common.exceptions import AttributeError
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import time
import random
#import progressbar
from bs4 import BeautifulSoup
import bs4

delay = 3
chrome_options = Options()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
        '/Users/ericjames/Documents/Freelance/chromedriver/chromedriver',
        options=chrome_options)
driver.implicitly_wait(2)

driver.get('https://www.nadaguides.com/Boats/2017/Grady-White-Boats/180-FISHERMAN-CC_/32072308/Specs')

engine_manufacturer = driver.find_element_by_xpath("//*[contains(text(), 'Engine Manufacturer')]")
engine_parent = engine_manufacturer.find_element_by_xpath('..')
print(engine_parent.text)
