from googletrans import Translator

a = []
trans = Translator()
	#loved public television series Sesame Street, will be creating children&#8217;s TV programs for <a class=\"crunchbase-link\" href=\"https://www.crunchbase.com/organization/apple/\" target=\"_blank\" data-type=\"organization\" data-entity=\"apple\">Apple <span class=\"crunchbase-tooltip-indicator\"></span></a>.</p>\n<p>The partnership will involve multiple shows, including live action and animated series, as well as a show with puppets. The deal does not include Sesame Street.</p>\n<p>I&#8217;m guessing that many (most? all?) of you watched Sesame Street on the public TV network PBS, where it still airs — but in 2015, <a href=\"https://www.newyorker.com/culture/on-television/the-evolution-of-sesame-street-on-hbo\">Sesame Workshop made a five-year deal</a> where episodes are broadcast on HBO months before they make it to PBS.</p>\n<p>Apple, meanwhile, continues to make one big content deal after another — just this week, it <a href=\"https://techcrunch.com/2018/06/20/apple-picks-up-the-immigrant-anthology-series-little-america-for-its-streaming-service/\">placed a series order for Little America</a>, an anthology show about immigrants from Big Sick writers Kumail Nanjiani and Emily V. Gordon, as well as Office producer Lee Eisenberg and Master of None producer Alan Yang.</p>\n<p>Unless you count unscripted efforts like Carpool Karaoke and Planet of the Apps, none of these announced shows have actually launched yet. Apple reportedly plans to launch the first wave of its original content initiative<a href=\"https://techcrunch.com/2018/03/26/apples-original-shows-may-launch-next-march-report-says/\"> in March of next year</a>, presumably as part of a new subscription streaming service.</p>\n<p>And while it&#8217;s also been reported that <a href=\"https://mashable.com/2017/10/25/apple-original-content/\">Apple is focused on funding family-friendly shows</a> (as opposed to the edgier fare that you might find on Netflix or HBO), this is time it&#8217;s announced programming created specifically for kids.</p>\n"
def chan(tex,i):
	a = trans.translate(tex,dest=i,src="en").text
	return a

def getMeComments(comments,x):
	d = []
	for i in range(0,x):
		d.append((comments[i]["author_name"],comments[i]["content"]["rendered"]))
	return d
	

def getTransList(comments,i):
	c_change = []
	for c in comments:
		print(len(c[1]))
		if len(c[1]) < 2000:
		 	c_change.append( (c[0],trans.translate(c[1],dest=i,src="en").text))
	return c_change

def getMeString(cList):
	st = ""
	for c in cList:
		st +=c[0]
		st += '\n'
		st += c[1]
		st+='\n'
	return st;		
