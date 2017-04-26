#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import sys
from urllib.request import urlopen
from pprint import pprint
import http

class myGithubRepos:
	githubUserName = ''
	fileName = ''

	def __init__(self, githubUserName):
		self.githubUserName = githubUserName
		self.fileName =  githubUserName+'_repos.json'
		print('ohyeah')

	def collectRepos(self):
		print('*** Collecting public for user ' + self.githubUserName)

		u = urlopen('https://api.github.com/users/'+self.githubUserName+'/repos')
		resp = json.loads(u.read().decode('utf-8'))
		#pprint(resp)
		return resp

	def writeToFile(self, data):
		print('*** Writing to file ' + self.fileName)

		#json_str = json.dumps(data)
		with open(self.fileName, 'w') as f:
			json.dump(data, f,indent=4)
		#print(data)

##########################

def main():
	grabUser = False
	for arg in sys.argv: # Akk, hairy stuff øøøø
		if arg == '-u':
			grabUser = True # read the next as username
			continue
		elif grabUser == True:
			userName = arg
			grabUser = False
	
	try:
	  userName
	except NameError:
	  print('No user name has been given, please use \'-u <uName>\'')
	  sys.exit()

	repos = myGithubRepos(userName)
	repo_json = repos.collectRepos()

	
	print(len(repo_json))

	#repos.writeToFile(repo_json)



if __name__ == '__main__':
   main()