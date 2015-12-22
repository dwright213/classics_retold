# standard libraries
from IPython import embed
from flask import Flask, jsonify, render_template, url_for, request
from imgurpython import ImgurClient
import os
import json
import pytumblr
import oauth
import sqlite3
import re
import random
import imghdr
import requests

# sqlite database connection
def sqlite_connect(toggle):
    conn = sqlite3.connect('moby_sentences.practice_delete.sql')
    c = conn.cursor()
    if toggle == True:
        return c
    elif toggle == False:
        conn.commit()
        conn.close()

def vacuum_sqlite():
    c.execute("VACUUM")

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tumblr_info')
def get_tumblr_info():
    client = pytumblr.TumblrRestClient(
        app.config['CONSUMER_KEY'],
        app.config['CONSUMER_SECRET'],
        app.config['OAUTH_TOKEN'],
        app.config['OAUTH_SECRET'],
    )
    return jsonify(client.info())

@app.route('/images', methods=['POST'])
def get_images():
    search_string = request.form['text']
    # fire up the ol' imgur client..
    client = ImgurClient(app.config['IMGUR_CLIENT_ID'], app.config['IMGUR_CLIENT_SECRET'])
    results = client.gallery_search(search_string, advanced=None, sort='time', window='all', page=0)
    results_dict = {}
    for count, result in enumerate(results):
        results_dict[count] = str(result.link)
        print str(result.link)
    return jsonify(results_dict)

@app.route('/sqlite/count')
def count_sentences():
    c = sqlite_connect(True)
    count_entries = "SELECT count(sent_text) AS count FROM sentences_grabbed"
    sentence_number = c.execute(count_entries).fetchmany()
    sqlite_connect(False)
    return render_template('count.html', count=sentence_number[0])

@app.route('/sqlite/get', methods=['POST'])
def get_sentence():
    record_number = request.form['number']
    c = sqlite_connect(True)
    get_sentence = "SELECT * FROM sentences_grabbed WHERE ROWID =?"
    sentence_got = c.execute(get_sentence,(record_number,)).fetchone()
    sqlite_connect(False)
    return render_template('sentence_got.html', sentence=sentence_got)

@app.route('/sqlite/delete/<record_number>')
def delete_sentence(record_number):
    conn = sqlite3.connect('moby_sentences.practice_delete.sql')
    c = conn.cursor()
    delete_sentence = "DELETE FROM sentences_grabbed WHERE ROWID =?"
    c.execute(delete_sentence,(record_number,))
    sqlite_connect(False)
    return str('sentence number '+ record_number +' deleted! ')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
