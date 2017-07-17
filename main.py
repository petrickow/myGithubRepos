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

	username = extractAndValidateArgs() # TODO return a list/dict instead
	repo_json = collectReposFor(username) # TODO check if username is valid
	reduced_data = reduceData(repo_json) # TODO traverse json and get the interesting bits
	writeJSONToFile(username+'_repos.json', reduced_data) # TODO write to file and
	pushToBlog(username+'_repos.json')# TODO upload to github-pages repo

### 
# Ask github for public repos and return as list
def collectReposFor(username):
	print('*** Collecting public repos, username: ' + username)

	u = urlopen('https://api.github.com/users/'+username+'/repos')
	resp = json.loads(u.read().decode('utf-8'))
	print('\tpublic repos found for ' + username + ':' , len(resp))
	return resp


### 
# TODO
# Boil the list down to active repos
def reduceData(orginial_json):
	print('Extract name and activity, maybe some more')
	print('list length: {}'.format(len(orginial_json)))
	reduced_repo_information = [];
	for entry in orginial_json:
		reduced_repo_information.append(getRepoDetails(entry));
		# TODO: Get more info, store the following:
		## * Language
		## * Activity
		## * Last commit date
		## * ???
	return reduced_repo_information

### 
# Stores data as json-file
def writeJSONToFile(filename, data):
	print('*** Writing to results/' + filename)
	with open('results/' + filename, 'w') as f:
		json.dump(data, f,indent=4)


def pushToBlog(filename):
	# TODO:
	print('push the file \'' + filename + '\' stuff to the repo')


def getRepoDetails(entry):
	# Create empty dict, save the useful stuff
	return({'name': entry['name'], 'language': entry['language'], 'description': entry['description']})

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
	try:
		username
	except NameError:
		print('No user name has been given, please use \'-u <uName>\'')
		sys.exit()

	return username


if __name__ == '__main__':
   main()
