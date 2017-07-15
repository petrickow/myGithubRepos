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
	username = extractAndValidateArgs()
	repo_json = collectReposFor(username)
	reduced_data =reduceData(repo_json)
	writeToFile(username+'_repos.json', repo_json)

### 
# Ask github for public repos and return as list
def collectReposFor(username):
	print('*** Collecting public repos, username: ' + username)

	u = urlopen('https://api.github.com/users/'+username+'/repos')
	resp = json.loads(u.read().decode('utf-8'))
	#pprint(resp) # if you want to see the result... you don't
	print('\tpublic repos found for ' + username + ':' , len(resp))
	return resp


### 
# TODO
# Boil the list down to active repos
def reduceData(orginial_json):
	reduced_info = list()
	current_obj = {}

	return ''

### 
# Stores data as json-file
def writeToFile(filename, data):
	print('*** Writing to results/' + filename)

	with open('results/' + filename, 'w') as f:
		json.dump(data, f,indent=4)
	#print(data)


def pushToBlog():
	#TODO
	print('push stuff to the repo')


### 
# Reads arguments and tries to find username
def extractAndValidateArgs():
	grabUser = False
	for arg in sys.argv: ## TODO: skip check on filename
		if arg == '-u':
			grabUser = True # read the next as username
			continue
		elif grabUser == True:
			username = arg
			grabUser = False
		else:
			print('Unknown argument "' + arg + '"')
	print(http.client)
	try:
		username
	except NameError:
		print('No user name has been given, please use \'-u <uName>\'')
		sys.exit()

	return username


if __name__ == '__main__':
   main()
