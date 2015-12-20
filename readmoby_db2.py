#!/usr/bin/python
import sqlite3
import re
import random
import kickaround

# def readData(z):
# 	for row in c.execute(sql, [
# 		a = (str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace('\\n',' ').replace('u"','"')).replace("\\","'")
# 		finaltext = a.replace('.,','.').replace('",','"').replace('!,','!').replace('?,','?')
#
# 		ism_spotter = bool(re.search('(?i)black?.\W|esquimaux|negro|indian|native|queequeg|race|slave|savage|cannibal|jew|islander|white', finaltext))
# 		longest_word = max(finaltext.split(), key=len)
# 		propernoun_guard = bool(re.search('[A-Z]', longest_word))
#
#
# 		if (ism_spotter == True):
# 			print (longest_word)
# 			randomImgsearch = random.randrange(999, 9999)
# 			kickaround.imageGrab(randomImgsearch, (randomImgsearch + 5), 'ismflag')
# 			morbydreck.makePost(entry_number, finaltext, 0, 'trigger warning')
# 			print (finaltext)
# 			print ('''
#
# 			''')
#
# 		if	(propernoun_guard == True and ism_spotter != True):
# 			print (longest_word)
# 			randomImgsearch = random.randrange(999, 9999)
# 			kickaround.imageGrab(randomImgsearch, (randomImgsearch + 5), 'nameflag')
# 			morbydreck.makePost(entry_number, finaltext, 0, 'namedrops')
# 			print (finaltext)
# 			print ('''
#
# 			''')
#
#
# 		elif (ism_spotter != True and propernoun_guard != True):
# 			print (longest_word)
# 			randomImgsearch = random.randrange(999, 9999)
# 			kickaround.imageGrab(randomImgsearch, (randomImgsearch + 5), longest_word)
# 			morbydreck.makePost(entry_number, finaltext, 0, 'terrible white whale')
# 			print (finaltext)
# 			print ('''
#
# 			''')



if __name__ == "__main__":
	conn = sqlite3.connect('moby_sentences.sql')
	c = conn.cursor()
	sql = "SELECT sent_text FROM sentences_grabbed WHERE ROWID =?"
	sql1 = "DELETE FROM sentences_grabbed WHERE ROWID =?"
	sql2 = "SELECT count(sent_text) AS count FROM sentences_grabbed"

	global entry_list
	global numberOfrows

	entry_list = []
	ism_list = ['black', 'negro', 'niger', 'indian', 'native', 'queequeg', 'race', 'slave', 'savage', 'cannibal', 'jew ', 'islander']
	finaltext = ''
	entry_number = 0
	numberOfrows = 1


def numberTherows():
	c.execute(sql2)
	global numberOfrows
	numberOfrows = str(c.fetchone()).replace('(','').replace(',','').replace(')','')
	global numberOfrows
	numberOfrows = int(numberOfrows)
	print('the number of rows is currently ' + str(numberOfrows))

def getList():
	global entry_list
	entry_list = range(0, numberOfrows)
	random.shuffle(entry_list)

def delEntry():
	c.execute(sql1,(entry_number,))

def stopNclean():
	print (numberOfrows)
	conn.commit()
	c.execute("VACUUM")
	conn.commit()
	conn.close()

# numberTherows()
# getList()
# for i in range(150):
# 	print ('posting number ' + str(i))
# 	print (entry_list[i])
# 	entry_number= (entry_list[i])
# 	readData(entry_number)
# 	delEntry()
# stopNclean()
