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
from imgurpython import ImgurClient




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
    # fire up the ol' imgur client..
    client = ImgurClient(app.config['IMGUR_CLIENT_ID'], app.config['IMGUR_CLIENT_SECRET'])
    results = client.gallery_search(search_string, advanced=None, sort='time', window='all', page=0)
    results_dict = {}
    for count, result in enumerate(results):
        results_dict[count] = str(result.link)
        print str(result.link)
    return jsonify(results_dict)

@app.route('/sqlite/count')
def search_database():
    conn = sqlite3.connect('moby_sentences.sql')
    c = conn.cursor()
    count_entries = "SELECT count(sent_text) AS count FROM sentences_grabbed"
    sentence_number = c.execute(count_entries).fetchmany()
    conn.close()
    return str(sentence_number)

@app.route('/sqlite/get/<record_number>')
def get_sentence(record_number):
    conn = sqlite3.connect('moby_sentences.sql')
    c = conn.cursor()
    get_sentence = "SELECT * FROM sentences_grabbed WHERE ROWID =?"
    sentence_got = c.execute(get_sentence,(record_number,)).fetchone()
    conn.close()
    return str(sentence_got)


if __name__ == "__main__":
    app.debug = True
    app.run()
