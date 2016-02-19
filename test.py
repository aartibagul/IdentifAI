import json
from clarifai.client import ClarifaiApi

clarifai_api = ClarifaiApi() # assumes environment variables are set.
response = clarifai_api.tag_images(open('/Users/aarti/Dropbox/instr1.jpg', 'rb'))
#parsed_json = json.loads(result)

print(response['results'][0]['result']['tag']['classes'][:6])
