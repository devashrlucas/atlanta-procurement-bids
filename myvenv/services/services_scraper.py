

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
long_phrase = ' The City of Atlanta'
long_phrase = long_phrase.decode('utf-8')


for url in urls:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    # returns list of NavigableStrings, cannot 'get' NS
    body = soup.find('body')

    for item in soup:
        for body_child in body.findChildren():
            if isinstance(body_child, NavigableString):
                pass
            elif body_child.name == 'footer':
                for entry in body_child:
                    for x in entry:
                        print x.name
            '''      
            else:
                for entry in body_child:
                    #full_item.append(entry)
                    #break
                    print "body_child ", body_child.name
                    print "entry ", entry.name
                    print entry
                    print '----'
            '''
        print '======'
'''
body_child  footer
entry  div
<div class="wrapper">
<div class="footer-col-wrapper">
<div class="disclaimer footer-disclaimer">
<p class="disclaimer">
'''


'''
for url in urls:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    #divs = soup.find_all('div')
    #paragraphs = soup.find_all('p')
    #footers = soup.find_all('footer')
    body = soup.find('body') #returns list of NavigableStrings, cannot 'get' NS
    divs = soup.find('div')
    for item in soup:
        for body_child in body.findChildren():
            if isinstance(body_child, NavigableString):
                pass
            elif body_child.name == 'header':
                pass
            elif body_child.name == 'div':
                for entry in body_child:
                    if entry.name == 'None':
                        pass
            elif body_child.name == 'a':
                for entry in body_child:
                    if entry.name == 'None':
                        pass
            elif body_child.name == 'nav':
                pass
            elif body_child.name == 'svg':
                pass
            elif body_child.name == 'strong':
                pass
            elif body_child.name == 'script':
                pass
            elif body_child.name == 'label':
                pass
            elif body_child.name == 'form':
                pass
            elif body_child.name == 'ul':
                for entry in body_child:
                    if entry.name == 'None':
                        pass
            elif body_child.name == 'h3':
                pass
            elif body_child.name == 'span':
                for entry in body_child:
                    if entry.name == 'strong':
                        pass
            elif body_child.name == 'select':
                pass
            elif body_child.name == 'option':
                pass
            elif body_child.name == 'button':
                pass
            elif body_child.name == 'footer':
                pass
            #elif ' 404.330.6204' in body_child:
                #pass
            elif body_child.name == 'li': 
                for entry in body_child:
                    if entry.name == 'strong':  # City of Atlanta
                        pass
            elif body_child.name == 'style':
                pass
            else:
                for entry in body_child:
                    #full_item.append(entry)
                    #break
                    print "body_child ", body_child.name
                    print "entry ", entry.name
                    print entry
                    print '-------------'
        print '====='

#Want to keep (* means some of these): h1, p, h2, *span (none), *ul (li), li (a), *li (None),p* (may need to do a list filtering for this)

#div.disclaimer for footer disclaimer

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
            else:
                ordered_list.append(body_child)
        print ordered_list
    ###### END OF THIS ONE 
'''                
'''
    for item in ordered_list:
        test_list = [item for item in ordered_list if time_phrase not in item 
                                                    if city_phrase not in item
                                                    if department_phrase not in item
                                                    if address_one_phrase not in item
                                                    if address_two_phrase not in item
                                                    if phone_one_phrase not in item
                                                    if fax_one_phrase not in item
                                                    if ' 404.658.7705' not in item
                                                    if ' 404.330.6204' not in item]                                               
        #print test_list
        #print '-------'
    ##### END OF THIS ONE
    
    for item in ordered_list:
        filtered_list = [item for item in ordered_list if time_phrase not in item 
                                                    if city_phrase not in item
                                                    if department_phrase not in item
                                                    if address_one_phrase not in item
                                                    if address_two_phrase not in item
                                                    if phone_one_phrase not in item
                                                    if fax_one_phrase not in item
                                                    if ' 404.658.7705' not in item
                                                    if ' 404.330.6204' not in item] 
    print filtered_list
    print '--------'
    ##### END OF THIS ONE
    
        
#h1: Title (key)
#h2: subheadings (keys)     



            for entry in item:
                filter(lambda entry: entry.get(
                    'class', '') != ['modal-footer'], full_item)
                print full_item
    ##### END OF THIS ONE

        for item in full_item:
            for entry in item:
                if item.get('class', '') == ['modal-footer']:
                    filter(lambda entry: entry.get(
                        'class', '') != ['modal-footer'], full_item)
                else:
                    print entry
                    print '============================'
        print "##############"
    ##### END OF THIS ONE 

    


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
