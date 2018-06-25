
import time 
from googletrans import Translator

while True:
	text = "This needs to be fixed"
	trans = Translator()
	print(trans.translate(text,dest="hi").text)
	time.sleep(15)
