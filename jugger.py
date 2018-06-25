
import time 
from googletrans import Translator
count = 0
while True:
	text = "This needs to be fixed"
	trans = Translator()
	print(trans.translate(text,dest="hi").text)
	print(count)
	count += 1
	time.sleep(15)
