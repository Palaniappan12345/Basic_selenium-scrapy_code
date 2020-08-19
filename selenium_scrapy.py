# import web driver
import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/home/palaniappan/Documents/selenium&scrapy/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_name
username = driver.find_element_by_name('session_key')

username.send_keys(parameters.linkedin_username)
sleep(0.5)


# locate password form by_name

password = driver.find_element_by_name('session_password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)


# locate submit button by_class_name
sign_in_button = driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button')

# .click() to mimic button click
sign_in_button.click()
sleep(0.5)

#open google url
driver.get('https:www.google.com')
sleep(1)

# locate search form by_name
search_query = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search_query.send_keys(parameters.search_query)
sleep(0.5)

# send_keys() to simulate the search text key strokes
search_query.send_keys(Keys.RETURN)
sleep(3)


# locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

# variable linkedin_url is equal to the list comprehension 
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

# to print all elements within our list 
print(linkedin_urls)

    
for url in linkedin_urls:
    
    driver.get(url)
   # add a 5 second pause loading each URL
    sleep(2)

   # assigning the source code for the webpage to variable sel
    sel = Selector(text = driver.page_source) 

    name = sel.xpath('//*[@id="ember51"]/div[2]/div[2]/div[1]/ul[1]/li[1]').extract_first()
    if name:
        name = name.strip()

    job_title = sel.xpath('//*[@id="ember51"]/div[2]/div[2]/div[1]/h2').extract_first()
    if job_title:
        job_title = job_title.strip()

    company = sel.xpath('//*[starts-with(@class,"pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()

    if company:
        company = company.strip()


# xpath to extract the text from the class containing the college
    college = sel.xpath('//*[starts-with(@class,"pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()

    if college:
        college = college.strip()


# xpath to extract the text from the class containing the location
    location = sel.xpath('//*[starts-with(@class,"pv-top-card-section__location")]/text()').extract_first()

    if location:
        location = location.strip()




    url = driver.current_url

    print('\n')
    print('Name: ', name)
    print('Position: ', job_title)
    print('Company: ', company)
    print('Education: ', college)
    print('Location: ', location)
    print('URL: ', url)
    print('\n')









