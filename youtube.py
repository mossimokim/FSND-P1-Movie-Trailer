import json
import requests

class Youtube():
	def __init__(self):
		# youtube API 3.0
		# refer to documentation for details
		# https://developers.google.com/youtube/v3/docs/search/list

		self.part = 'snippet'
		self.key = 'AIzaSyAxBU-kC0acCmlvfQ4lPSTHlKBeAYQmnzk' #replace with your API key
		self.maxResults = '12'
		self.order = 'viewCount' # we are sorting by popularity
		self.search = '' # we will set this before pulling list from youtube
		self.vtype = 'video'
		self.videoDefinition = 'high' # we would like to watch 720P or higher video, right?

	def load(self):
		self.query = 'https://www.googleapis.com/youtube/v3/search?part=' + self.part + \
					'&maxResults=' + self.maxResults + \
					'&order=' + self.order + \
					'&q=' + self.search + \
					'&type=' + self.vtype + \
					'&videoDefinition=' + self.videoDefinition + \
					'&key=' + self.key
		response = requests.get(self.query)
		self.data = json.loads(response.text)
