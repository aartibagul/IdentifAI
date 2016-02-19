from clarifai.client import ClarifaiApi
import sys
import os
import shelve

shelf = shelve.open('tag_shelf')

directory_path = str(sys.argv[1]) #get the directory path
clarifai_api = ClarifaiApi() # assumes environment variables are set.


for f in os.listdir(directory_path):
    if f.endswith(".png") or f.endswith(".jpeg") or f.endswith(".jpg") :
        image_path =  str(os.path.join(directory_path,f))
        response = clarifai_api.tag_images(open(image_path, 'rb'))
        tag_list = response['results'][0]['result']['tag']['classes'][:6]

        for t in tag_list:
            if shelf.has_key(t):
                if image_path not in shelf[t]:
                    temp = shelf[t]
                    temp.append(image_path)
                    shelf[t] = temp
            else:
                shelf[t] = [image_path]

print(shelf)
shelf.close()







