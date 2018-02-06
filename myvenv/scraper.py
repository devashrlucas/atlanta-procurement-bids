from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

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


for url in LinkList:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    print soup.prettify()




'''
box = driver.find_element_by_xpath('//*[@id="project-solicitations"]')
options = box.find_element_by_css_selector('.btn')
for option in options:
    print option
'''



''' LISTS TITLES
box = driver.find_element_by_xpath('//*[@id="project-solicitations"]')
print box.text
'''

'''PRINTS LIST OF IDS
options = box.find_elements_by_tag_name('option')
optionsList = []

for option in options:
    #optionsList.append(option.get_attribute('value'))
    if option.get_attribute('value') != 'blank':
        optionsList.append(option.get_attribute('value'))
        
print optionsList
'''



'''BS
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
print soup.prettify()
'''







"""
Flow:
if option value is not blank:
    for each option:
        click get more information ('//*[@id="project-more-info-link"]')
        get info from project-info-well OR scrape the new URL in a seperate tab
        capture new URL and save it to a list
run URLs in list through function to scrape data? (may not need SE for that partt)

"""
