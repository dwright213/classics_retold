import pytumblr
import oauth
import os

client = pytumblr.TumblrRestClient(
app.config['CONSUMER_KEY'],
app.config['CONSUMER_SECRET'],
app.config['OAUTH_TOKEN'],
app.config['OAUTH_SECRET'],
)

client.info() # Grabs the current user information

#for i in range(0, 5, 1):
def makePost(ti, bo, imgnum, flag):

	#client.create_photo('codingjester', state='draft', tags=['jb is cool'], format='markdown', data=['/Users/johnb/path/to/my/image.jpg', '/Users/johnb/Pictures/kittens.jpg'], caption='## Mega sweet kittens')
	#Creates a photo post using a local filepath

	client.create_photo('classicsretold',
						state='queue',
						tags=[str(ti), str(flag), 'literature', 'books', 'whales', 'sperm whale', 'classics re.told'],
						tweet='Moby Machinations',
						data='/home/dan/python-scripts/images/' + str(imgnum) + '.jpeg', caption=bo)

	os.remove('/home/dan/python-scripts/images/' + str(imgnum) + '.jpeg')

	#client.create_photo('chizborg', state='queue', tags='ti', caption='bo', data='/home/dan/python-scripts/images/Les_Horribles_Cernettes_in_1992.jpg')


	#client.create_text('chizborg', state = 'queue', slug = ti, title=ti, body = bo)
