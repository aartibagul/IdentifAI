# IdentifAI
Search for images  in your file system by assigning tags

IdentifAI uses the ClarifAI API to tag pictures in a directory (specified by the user) and saves the mapping between the tags and the paths of the images in a python shelve. This allows the user to then search for images with a specific tag.

##Usage##
```./run.sh -c tag -d /path/to/directory ```tags all the images in the directory and saves the tags. 

 ```./run.sh -c search ```allows the user to search for images that have been tagged.

NOTE: You must first follow the installation steps listed on the [Clarifai Python API client] (https://github.com/Clarifai/clarifai-python). 

 ```
pip install git+git://github.com/Clarifai/clarifai-python.git
export CLARIFAI_APP_ID=<an_application_id_from_your_account>
export CLARIFAI_APP_SECRET=<an_application_secret_from_your_account>
 ```

##Future work##
- Go through directories recursively in order to access images in sub-directories
- Group similar images together
- Let users have the option to get similar images from the web
- Embed the tags in the image metadata and make the tags searchable through Finder in Mac OS X
- Improve the user experience (example - show previews of images instead of image paths)
 

##Special Thanks##
To Giorgio who came up with the idea, and the name, with his brilliant creativity.
