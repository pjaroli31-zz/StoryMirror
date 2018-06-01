from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

def getName(url):
	option = webdriver.ChromeOptions()
	option.add_argument('--incognito')

	browser = webdriver.Chrome(executable_path='C:/Users/pulkit/Downloads/chromedriver_win32/chromedriver', chrome_options=option)
	browser.get(url)
	i = 1
	while (i < 4):
		WebDriverWait(browser,60000)
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		html = browser.page_source
		soup = BeautifulSoup(html,"html.parser")
	# print(soup.prettify)
		#print('balalalal')
		i += 1		
	browser.quit()	
	b_name = soup.find_all('div',{'class':'Book__bookTitle___2vtsy'})[0].text
	return b_name	
