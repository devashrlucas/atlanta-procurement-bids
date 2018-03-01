
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, NavigableString
import requests
import simplejson as json
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


'''   DONE --- LEAVE THIS ALONE
url = 'http://procurement.atlantaga.gov/solicitations/'


driver = webdriver.Chrome()

driver.get(url)
delay = 15


try:
    element = WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="project-departments"]'))).click()
    element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[2]/p[3]/select/option[2]'))).click()
    element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="product-category-cs"]'))).click()
    element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div[2]/p[4]/select/option[2]'))).click()
except TimeoutException:
    print "Failed"


#box = driver.find_element_by_xpath('//*[@id="project-more-info-link"]')
box = driver.find_element_by_xpath('//*[@id="project-solicitations"]')
options = box.find_elements_by_tag_name('option')
delay = 20

LinkList = []
for option in options:
    try:
        element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="project-solicitations"]')))
        option.click()
        element = WebDriverWait(driver, delay).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="project-more-info-link"]')))
        div = driver.find_element_by_id('project-more-info-link')
        link = div.find_element_by_css_selector('a').get_attribute('href')
        LinkList.append(link)
    except (TimeoutException, StaleElementReferenceException):
        pass


# MAY HAVE TO CHANGE THIS LATER
with open('services_urls.txt', 'w+') as f:
    for url in LinkList:
        f.write('\n'.join(LinkList))
    f.close()
'''

f = open('services_urls.txt', 'r')
urls = (line.strip() for line in f)



def get_info(url):
    #global full_set
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'lxml')
        body = soup.find('body')
        for item in soup:
            to_keep = []
            keep_copy = {} 
            if isinstance(item, NavigableString):
                pass
            for item in body:
                if item.name == 'div':
                    for entry in item:
                        if entry.name == 'div':
                            if entry.get('class', '') == ['wrapper']:
                                    pass 
                            for item in entry.findChildren(): #returns a list
                                if item.name == 'div':
                                    for entry in item:
                                        if entry.name == 'h1':
                                                        to_keep.append(
                                                re.sub('<[^>]*>', '', str(entry)))
                                        if entry.name == 'p':
                                            to_keep.append(
                                                re.sub('<[^>]*>', '', str(entry)))
                                        if entry.name == 'h2':
                                            to_keep.append(
                                                re.sub('<[^>]*>', '', str(entry)))
                                        if entry.name == 'ul':
                                            to_keep.append(
                                                re.sub('<[^>]*>', '', str(entry)))
                                        #if 'a conflict or discrepancy between the information or documents' in str(entry):
                                                #pass  
                                    keep_copy = {key: value for key, value in enumerate(to_keep)}
                                    #get_info.keep_copy = keep_copy #function attribute?
                                    get_info.full_set = {}
                                    get_info.full_set.update(keep_copy)
                                    return get_info.full_set
                                    #get_info.full_set
                            
                                    '''
                                    testing = ['123','234','546']
                                    return testing
                                        '''

'''
for url in urls:
    get_info()
    print get_info.full_set
'''   



"""
Notes:
Quicker to store dictionary in sqlalchemy then use flask to access?
Need to run scraper to get keep_copy for app.py?
Function wrapper to add function attribute to be able to a call in app.py?
"""
