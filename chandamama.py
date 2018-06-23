from googletrans import Translator
from trans import *
import requests
import json
import csv
eng  = list()
hi = list()
gu = list()
bn = list()
mr = list()
img_url = ""
dest_lang = ["hi","bn"]
trans = Translator()
url = "https://techcrunch.com/wp-json/tc/v1/magazine"

for i in range(2,100):
    querystring = {"page":str(i),"_embed":"true"}
    print(i)
    headers = {
        'Host': "techcrunch.com",
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        'Accept': "*/*",
        'Accept-Language': "en-GB,en;q=0.5",
        'Referer': "https://techcrunch.com/",
        'content-type': "application/json; charset=utf-8",
        'origin': "https://techcrunch.com",
        'Cookie': "rxx=18k6csjsh1.15nlyxfc&v=1; _ga=GA1.2.348114864.1529062901; __adblocker=false; _parsely_visitor={%22id%22:%22001eded6-06df-4f26-a5f4-d334680a079a%22%2C%22session_count%22:4%2C%22last_session_ts%22:1529565473122}; __tbc=%7Bjzx%7DjGAToaZMxJYLoS7N4KRjDfEJqMXQn2jSca-VGknLasw_o4iSSFv-gF1dEJDhLR1PVkg2sRnhpo3RlGP5zDTugRFH4WwUTRWJbUcTaE-dfCB5e9pt8AbZOgiHxFFqy8SROzaeIILFhlSTw5lulLLvTw; __pat=-14400000; xbc=%7Bjzx%7D_e5BhmMRjtsjUjGbrtX0c7h7R3xM4VwABoRuGqnXs1Ch_5rnoQguNFJyyQn8ud-iL8IqeSU80X8vYQUgLUhfHuPrqkFUD8LP3EfB-GmoSaJPVXX_V2A91n1EaBr6LYFcVVVRxJYt27eXvfrqH_9lRmfTioQRNgR1hd-KydO9JaI; __pnahc=0; GUC=AQEBAQFbK_9cEEIfAQSH&s=AQAAAGW24p6D&g=Wyq5cQ; BX=5ek3m6tdileb7&b=3&s=8d; __pcvc={}; __pvi=%7B%22id%22%3A%22v-2018-06-21-13-14-39-441-AZxZb0bh7hjW7P1l-afcd61c3e3106f87c2fde9b5d021077a%22%2C%22domain%22%3A%22.techcrunch.com%22%2C%22time%22%3A1529567079441%7D; _gid=GA1.2.394305117.1529526634; cmp=t=1529567085&j=0; _parsely_session={%22sid%22:4%2C%22surl%22:%22https://techcrunch.com/%22%2C%22sref%22:%22https://techcrunch.com/2005/06/11/technorati-new-improved/%22%2C%22sts%22:1529565473122%2C%22slts%22:1529526634287}; _gat=1",
        'Connection': "keep-alive",
        'Cache-Control': "no-cache",
        'Postman-Token': "d7b01640-9aaf-4199-a4ca-6f44da0f022b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    json_data = response.text
    json_as_dict = json.loads(json_data)
    for item in json_as_dict:
        p_id = item["id"]
        print(p_id)
        date = item["date"].split('T')[0]
        time = item["date"].split('T')[1]
        tex = item["content"]["rendered"]
        authors = item["_embedded"]["authors"]
        if "wp:featuredmedia" in item["_embedded"]:
            img_url = item["_embedded"]["wp:featuredmedia"][0]["source_url"]
        #print(img_url)
        t = ""
        tag_list = item["_embedded"]["wp:term"]
        for tag in tag_list:
            for x in tag:
                t += x["name"]+'\n'
       # print(t)        
        author_name = []
        for a in authors:
            author_name.append(a["name"])
            #print(a["name"])
       # print(len(tex))
        title = item["title"]["rendered"]
        link = item["shortlink"]
        
        lan_title = []
        getT = ""
        countT = int(len(title)/500)
        for k in range(0,2):
            for num in range(0,countT):
                getT += chan(title[500*num:500 *(num+1)],dest_lang[k])
            getT += chan(tex[500 * countT : len(title)-1],dest_lang[k])
            lan_title.append(getT)
            getT =""
        count = int(len(tex)/500)
        #print(len(tex))
        lan_content = []
        getC =""
        for idx in range(0,2):
            for num in range(0,count):
                getC += chan(tex[500 * num : 500 * (num+1)],dest_lang[idx])
           
            getC += chan(tex[500 * count : len(tex)-1],dest_lang[idx])   
            lan_content.append(getC)
            getC = ""

        url2 = "https://techcrunch.com/wp-json/wp/v2/comments?post="+str(p_id)+"&order=asc&tc_hierarchical=flat"
        comm_response = requests.request("GET",url2)
        comm_as_dict = json.loads(comm_response.text)
        co = []
       # print(len(comm_as_dict))
        if len(comm_as_dict) >0:
            co = getMeComments(comm_as_dict,min(4,len(comm_as_dict)))
       # print(co)    
        cstring = getMeString(co)
        eng.append((date,time, title,author_name,tex,link,cstring,img_url,t))
        cList = getTransList(co,"hi")
        cstring = getMeString(cList)    
        hi.append((date,time, lan_title[0],author_name,lan_content[0],link,cstring,img_url,t))
        cList = getTransList(co,"bn")
        cstring = getMeString(cList)
        bn.append((date,time, lan_title[1],author_name,lan_content[1],link,cstring,img_url,t))
        '''
        cList = getTransList(co,"gu")
        cstring = getMeString(cList)
        gu.append((date,time, lan_title[2],author_name,lan_content[2],link,cstring,img_url,t))
        cList = getTransList(co,"mr")
        cstring = getMeString(cList)
        mr.append((date,time, lan_title[3],author_name,lan_content[3],link,cstring,img_url,t))    
        '''
        #print(cList)

for d in eng:
    with open("check.csv","a",newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(d)

for d in bn:
    with open("Bengali.csv","a",newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(d)


for d in hi:
    with open("Hindi.csv","a",newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(d)


'''
for d in gu:
    with open("gujrati.csv","a",newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(d)
for d in mr:
    with open("marathi.csv","a",newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerow(d)                    
      
'''
