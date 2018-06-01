import json
from getBookName import getName 
import requests
from bs4 import BeautifulSoup
import csv

headers = {
        'authority': "www.juggernaut.in",
        'pragma': "no-cache",
        'Cache-Control': "no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'cookie': "languageFilter__PRODUCTION__={\"id\":\"english\",\"title\":\"English\",\"value\":\"english\",\"shortTitle\":\"EN\"}; readingConfig={\"font-size\":\"20px\",\"line-height\":\"normal\",\"color-theme\":\"normal\"}; deviceFingerPrint__PRODUCTION__=94a16745d59123257a3c0a5cb30816e1; _ga=GA1.2.1556833857.1527775697; _gid=GA1.2.1002499830.1527775697; WZRK_G=545c79121db244c9bfceed4ec7ff9951; userIPAddress__PRODUCTION__=103.85.133.9; _gat=1; WZRK_S_R5Z-ZRK-454Z=%7B%22p%22%3A1%2C%22s%22%3A1527791086%2C%22t%22%3A1527791096%7D",
    }

def printCSV(urls):
    

    for each_url in urls:
        b_name = getName(each_url)
        response = requests.request("GET", each_url+'/reviews', headers=headers)
        response_soup = BeautifulSoup(response.text, 'html.parser')

        script_list = response_soup.find_all("script")

    

        json_data = script_list[8].text[27:]
        json_as_dict = json.loads(json_data)

        print("AUTHORS:")
        json_dict_authors = json_as_dict['reduxAsyncConnect']['jsonLinkedData']['authors']
        ## Author(s) data:
        # Let's first get that random string which is key in dict:
        for item in json_dict_authors:
        # Now let's get author's name and email
            with open('Authors.csv','a',newline='') as fi:
                fiW = csv.writer(fi)
                fiW.writerow([json_dict_authors[item]['name'],  json_dict_authors[item]['email_address'],b_name,each_url])
            
        ## Data of readers who commented:
        print("REVIEWERS:")
        json_dict_reviews = json_as_dict['reduxAsyncConnect']['jsonLinkedData']['reviews']['user_reviews']
        if len(json_dict_reviews) == 0:
            print("    --NA--")
        for item in json_dict_reviews:

            with open('Users.csv','a',newline='') as fu:
                fuW = csv.writer(fu)
                fuW.writerow([item['user']['first_name'], item['user']['last_name'],item['user']['email_address']])
            


    