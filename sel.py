from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

option = webdriver.ChromeOptions()
option.add_argument('--incognito')

browser = webdriver.Chrome(executable_path='C:/Users/pulkit/Downloads/chromedriver_win32/chromedriver', chrome_options=option)
browser.get('https://hindi.pratilipi.com/articles-home')
i = 1
while (i < 21):
	WebDriverWait(browser,60000)
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	html = browser.page_source
	soup = BeautifulSoup(html,"html.parser")
	# print(soup.prettify)
	print('balalalal')
	i += 1

#browser.quit()

spans = soup.find_all('div',{'class':'pratilipi'})
count = 0
for i in spans:
	a = i.find_all('a')[0]
	count+=1
	print(a['href'])
print(count)
