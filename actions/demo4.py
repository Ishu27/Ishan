import requests

from st2common.runners.base_action import Action

class abc(Action):
	
	def run(self, url):
		
		try:
			response = requests.get(url)
			print(response.status_code)
			print(response.url)
			
		except requests.exception.MissingSchema:
			print("Wrong URL")
			sys.exit(0)
			
			
			
