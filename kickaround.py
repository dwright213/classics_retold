#!/usr/bin/python3
import requests
#maxRe = requests.adapters.HTTPAdapter(max_retries=0)
import json
import imghdr
import random

#pages = ["0", "4", "8", "12", "16", "20", "24", "28"]
#page = 0
#count = 1000

def imageGrab(begin, end, longstring):
	pages = ["0", "4", "8", "12", "16", "20", "24", "28"]
	i = 0

	while (begin < end):
		page = random.randrange(0, 7)
		while page < 8:
			if longstring == 'ismflag' or longstring == 'nameflag':
				resp = requests.get('http://ajax.googleapis.com/ajax/services/search/images?imgtype=hires&v=1.0&as_rights=(cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived)&q=dscf+OR+img_+OR+dsc+OR+dsc0+OR+-camera+"' + str(begin) + '&start=' + pages[page])
			else:
				resp = requests.get('http://ajax.googleapis.com/ajax/services/search/images?imgtype=hires&v=1.0&q=dscf+OR+img_+OR+dsc+OR+dsc0+OR+-camera+"' + str(begin) + '+OR+' + longstring + '&start=' + pages[page])
			#resp = requests.get('http://ajax.googleapis.com/ajax/services/search/images?imgtype=hires&v=1.0&q=istockphotos ' + str(begin) + '&start=' + pages[page])
			#stick this line in the above to get pretty safe, wikipedia (mostly) images:  &as_rights=(cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived)
			jsonData = json.loads(resp.text)
			searchResults = jsonData['responseData'] ['results']
			if searchResults != None:
				for item in searchResults:
					print ('checking for usable images...')
					width = int(item['width'])
					title = item['title']
					link = item['url']
					if width > 1000:
						print ('we are at page ' + str(page) + ' of the results for searching ' + str(begin))
						print (title)
						print (link)

						try:
							imageGot = requests.get(link, timeout=3)
						except:
							imageGot = 'None'
							print ('oh no, problems!')
							print ('''

								''')



						if imageGot != 'None':
							print ('verifying image...')
							imgext = imghdr.what('',imageGot.content)
							if str(imgext) == "jpeg":
								with open('images/' + str(i) + '.' + imgext, 'wb') as code:
									code.write(imageGot.content)
									return('image gotten!')
									i = i + 1
									print ('image successfully grabbed!')
									print ('''

										''')
			else:
				print ('oops! google/json dont wanna play ball. on to the next page.')
				print ('''

					''')
			page = page + 1
			#print page
		begin = begin + 1
	print ('hey, nice work u got like a shit ton of images now yay :D')

#imageGrab(421, 422)
