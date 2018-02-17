from bs4 import BeautifulSoup, NavigableString
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

full_item = []
filtered_item = []


unordered_list = []
nested_text = []
ordered_list = []

time_phrase = 'Mon-Fri, 8:15am - 5pm ET' #works
city_phrase = '<strong>City of Atlanta<br/>Department of Procurement</strong>'  # doesn't work
department_phrase = 'Department of Procurement'
address_one_phrase = '55 Trinity Avenue - Ste. 1900'
address_two_phrase = 'Atlanta, GA 30303'
phone_one_phrase = 'Phone:'
phone_two_phrase = ' 404.330.6204', #TypeError: coercing to Unicode: need string or buffer, tuple found
fax_one_phrase = 'Fax:'
fax_two_phrase = ' 404.658.7705' #TypeError: coercing to Unicode: need string or buffer, tuple found



f = open('services_urls.txt', 'r')
urls = (line.strip() for line in f)
   
for url in urls:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    #divs = soup.find_all('div')
    #paragraphs = soup.find_all('p')
    #footers = soup.find_all('footer')
    body = soup.find('body') #returns list of NavigableStrings, cannot 'get' NS
    #divs = soup.find('div')
    for item in soup:
        # START HERE: NEED TO REMOVE SOCIAL MEDIA W/O REMOVING OTHER <LI> #############
        for body_child in body.findChildren():
            if isinstance(body_child, NavigableString):
                pass
            elif body_child.name == 'header':
                pass
            elif body_child.name == 'site-footer': #doesn't work
                pass
            elif body_child.name == 'div':
                if body_child.get('class', '') == ['wrapper']:
                    pass
            elif body_child.name == 'p':
                if body_child.get('class', '') == ['disclaimer']:
                    pass
                else:
                    nested_text.append(body_child)
            elif body_child.name == 'ul':
                if body_child.get('class', '') == ['social-media-list']:
                    pass
                if body_child.get('class', '') == ['contact-list']: #doesn't work
                    pass
                else:
                    unordered_list.append(body_child)
            elif body_child.name == 'a':
                pass
            elif body_child.name == 'nav':
                pass
            elif body_child.name == 'svg':
                pass
            elif body_child.name == 'path':
                pass
            elif body_child.name == 'br':
                pass
            elif body_child.name == 'script':
                pass
            elif body_child.name == 'strong':
                pass
            elif body_child.name == 'iframe':
                pass
            elif body_child.name == 'label':
                pass
            elif body_child.name == 'form':
                pass
            elif body_child.name == 'input':
                pass
            elif body_child.name == 'span':
                pass
            elif body_child.name == 'option':
                pass
            elif body_child.name == 'svg':
                pass
            elif body_child.name == 'select':
                pass
            elif body_child.name == 'button':
                pass
            elif body_child.name == 'footer':
                pass
            elif body_child.name == 'img':
                pass
            elif body_child.name == 'style':
                pass
            elif body_child.name == 'link':
                pass  
            elif body_child.name == 'h3':
                pass  
            elif body_child in body.select('.contact-list'): #doesn't work
                pass 
            elif body_child.name == 'li':
                for entry in body_child:
                    if entry.name == 'a' and entry['href'] == 'https://twitter.com/atlprocurement':
                        pass
                    elif entry.name == 'a' and 'https://na01.safelinks.protection.outlook.com' in entry['href']:
                        pass
                    else:
                        ordered_list.append(entry)
            elif body_child.name == 'p':
                for entry in body_child:
                    if entry.get('class', '') == 'text':
                        pass
    for item in ordered_list:
        test_list = [item for item in ordered_list if time_phrase not in item 
                                                    if city_phrase not in item
                                                    if department_phrase not in item
                                                    if address_one_phrase not in item
                                                    if address_two_phrase not in item
                                                    if phone_one_phrase not in item
                                                    if fax_one_phrase not in item
                                                    if phone_two_phrase not in item]                                               
        print test_list
        print '-------'
     
           
        
#h1: Title (key)
#h2: subheadings (keys)     


'''
            for entry in item:
                filter(lambda entry: entry.get(
                    'class', '') != ['modal-footer'], full_item)
                print full_item
'''
'''
        for item in full_item:
            for entry in item:
                if item.get('class', '') == ['modal-footer']:
                    filter(lambda entry: entry.get(
                        'class', '') != ['modal-footer'], full_item)
                else:
                    print entry
                    print '============================'
        print "##############"
'''

    


    #if div.get('class', '') == div.get('class', 'modal-footer'):
                # continue


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
contact info seems to be automatic ---> give it a random key then filter it out or learn regex?
"""
