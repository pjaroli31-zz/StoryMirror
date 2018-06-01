from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from getBooks import getBook
from getData import printCSV
option = webdriver.ChromeOptions()
option.add_argument('--incognito')

browser = webdriver.Chrome(executable_path='C:/Users/pulkit/Downloads/chromedriver_win32/chromedriver', chrome_options=option)
browser.get('https://www.juggernaut.in/categories')
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

spans = soup.find_all('div',{'class':'CategoryList__box_list___2cKax'})
count = 0
aList = []
for i in spans:
	s = i.find_all('a')[0]['href']
	a = ('https://www.juggernaut.in'+ s)
	aList.append(a)
	#print(a['href'])
	count += 1
print(count)	
browser.quit()
bookList = []

for link in aList:
	bookList += getBook(link)

print("books are :printing")	
printCSV(bookList)
