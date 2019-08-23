import requests

from st2common.runners.base_action import Action

class abc(Action):
	response = request.get('https://google.com')
	def run(self, response):
		if response.status_code == 200:
        		print('Success!')
		elif response.status_code == 404:
    			print('Not Found.')
