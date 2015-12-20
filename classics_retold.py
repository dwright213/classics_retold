# standard libraries
from IPython import embed
from flask import Flask, jsonify
import os
import json
import pytumblr
import oauth
import sqlite3
import re
import random
import imghdr
import requests

# local modules
# import kickaround
# import readmoby_db2
# import tumblr_poster


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

@app.route('/')
def hello():
    return app.config['CONSUMER_KEY']

@app.route('/tumblr_info')
def get_tumblr_info():
    client = pytumblr.TumblrRestClient(
        app.config['CONSUMER_KEY'],
        app.config['CONSUMER_SECRET'],
        app.config['OAUTH_TOKEN'],
        app.config['OAUTH_SECRET'],
    )
    return jsonify(client.info())

@app.route('/images/<search_string>')
def get_images(search_string):
    google_api_string = 'http://ajax.googleapis.com/ajax/services/search/images?imgtype=hires&v=1.0&q=dscf+OR+img_+OR+dsc+OR+dsc0+OR+-camera+"' + str(2) + '+OR+' + search_string + '&start=' + str(2)
    resp = requests.get(google_api_string)
	#resp = requests.get('http://ajax.googleapis.com/ajax/services/search/images?imgtype=hires&v=1.0&q=istockphotos ' + str(begin) + '&start=' + pages[page])
	#stick this line in the above to get pretty safe, wikipedia (mostly) images:  &as_rights=(cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived)
	# jsonData = json.loads(resp.text)
    print google_api_string
    return str(resp)


if __name__ == "__main__":
    app.debug = True
    app.run()
