from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import simplejson as json

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


with open('services_urls.txt', 'r') as f:
    #lines = f.readlines()
    for line in f:
        response = requests.get(line)
        html = response.content
        soup = BeautifulSoup(html, 'lxml')
        
        
       
        divs = soup.find_all('div')
        paragraphs = soup.find_all('p')
        footers = soup.find_all('footer')

        #content = soup.find_all('div', {'class': 'page-content'})
        #form_content = soup.find_all('div', {'class': 'ninja-forms-cont'})
        #footer_content = soup.find_all('footer', attrs={'class': 'site-footer'})
       # disclaimer_content = soup.find_all('div', {'class': 'disclaimer'})
        modal_content = soup.find_all('div', {'class': 'modal-content'})
        wrapper_content = soup.find_all('div', {'class': 'wrapper'})

        for d in divs:
            #print item.get('class', '')
            #rint "----------------"
            if d.get('class', '') == ['modal-body']:
                modal_body = [d]
            if d.get('class', '') == ['ninja-forms-cont']:
                form_content = [d]
        for p in paragraphs:
            if p.get('class', '') == ['disclaimer']:
                disclaimer =  [p]
        for f in footers:
            if f.get('class', '') == ['site-footer']:
                footer = [f]
        '''
        for item in soup:
            for div in divs:
                for d in div:
                    if d.get('class', '') == ['bs4.element.Tag']:
                        print type(d)
                        print d
                        print '---------'
                    #if d.get('class','') == footer:
                        #print d
                       # print '---------'
        '''

        body = soup.find('body')
        
        
        for body_child in body.findChildren():
            if isinstance(body_child, NavigableString):
                continue
            else:
                print body_child
                print '------------'
           

       
       


            #title = soup.find_all('h1')
            #dict_keys = soup.find_all('h2')
            #print text
            #print title, dict_keys
           # print item
           # print '------------------------'
              

     
            #.page - content > div: nth - child(1) > div: nth - child(2) > p: nth - child(24)

############### NEED TEXT THAT ISN'T IN FOOT OR DISCLAIMER 
################# MAYBE IT DEPENDS ON HOW IT"S LOADED IN? AJAX? JSON? JS? JQUERY? I DON'T KNOW      
        

'''
#text = soup.find_all('p') NOT QUITE, ALSO RETURNS GREY TEXT (class="site-footer")
for item in soup:
    #print title, dict_keys, text
    print item
    print "--------------------------"
'''


'''
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    #print soup.prettify()

    content = soup.find_all("div", {"class": "page-content"})

    for div in content:
        print div
''' 


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

turn titles or <h2> into dict keys?
actual text is <p> but also using <p> blank for formatting
some of the text is #text w/o any tags or other CSS
proposal documemnts are <ul> or <li> and links(?)

"""
