# open chrome browser and launch the website
# on the search field enter keyword = 'selenium'
# verify product names in search result contains the keyword

from selenium import webdriver

# test data
browser_path = "..\chromedriver_win32\chromedriver.exe"
website_path = "https://www.google.com/"
keyword = 'selenium'

# initialize the browser
driver = webdriver.Chrome(browser_path)
driver.implicitly_wait(30)
driver.maximize_window()

# open the page and enter the keyword
driver.get(website_path)
search_field = driver.find_element_by_name('q')
search_field.send_keys(keyword)
search_field.submit()

# close the browser
# driver.quit()