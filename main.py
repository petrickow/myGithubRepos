#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import sys
from urllib.request import urlopen
from pprint import pprint
import http


###
# Getting started with python3
def main():
	username = extractArgs()
	
	repo_json = repos.collectReposFor(username)
	
	reduceData(repo_json)

#	writeToFile(username+'_repos.json')

### 
# Ask github for public repos and return as list
def collectReposFor(self, username):
	print('*** Collecting public repos, username: ' + username)

	u = urlopen('https://api.github.com/users/'+username+'/repos')
	resp = json.loads(u.read().decode('utf-8'))
	#pprint(resp)
	print(type(resp))
	return resp


###
# Boil the list down to active repos
def reduceData(orginial_json):
	reduced_info = list()
	current_obj = {}


	print(type(orginial_json))
	print(len(orginial_json))

	return ''

### 
# Stores data as json-file
def writeToFile(filename, data):
	print('*** Writing to file ' + filename)

	with open(filename, 'w') as f:
		json.dump(data, f,indent=4)
	#print(data)


### 
# Reads arguments and tries to find username
def extractArgs():
	grabUser = False
	for arg in sys.argv: # Akk, hairy stuff øøøø
		if arg == '-u':
			grabUser = True # read the next as username
			continue
		elif grabUser == True:
			username = arg
			grabUser = False
	print(http.client)
	try:
		username
	except NameError:
		print('No user name has been given, please use \'-u <uName>\'')
		sys.exit()

	return username


if __name__ == '__main__':
   main()