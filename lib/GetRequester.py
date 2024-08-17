import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):          
        
        # Send a GET request to the URL and return the content
        response = requests.get(self.url)
        return response.content
    

    def load_json(self):
        # Load the JSON content into a Python dictionary
        response_content = self.get_response_body()

        # Load the JSON content into a Python dictionary
        data = json.loads(response_content)
        
        return data