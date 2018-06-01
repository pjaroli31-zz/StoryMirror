from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup



def getBook(link):
	option = webdriver.ChromeOptions()
	option.add_argument('--incognito')
	browser = webdriver.Chrome(executable_path='C:/Users/pulkit/Downloads/chromedriver_win32/chromedriver', chrome_options=option)
	browser.get(link)
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

	spans = soup.find_all('div',{'class':'SearchContainer__book_content___m0GWt'})
	count = 0
	a = []
	for i in spans:
		a.append('https://www.juggernaut.in' + i.find_all('a',{'class':'SearchContainer__book_name___3JAWn'})[0]['href'])
		#print(a['href'])
		count += 1
	print(count)	
	browser.quit()
	return a



