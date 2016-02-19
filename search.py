import sys
import os
import shelve

shelf = shelve.open('tag_shelf')
if len(shelf.keys()) == 0:
    print("No images have been tagged. Please use run.sh with flag -c tag first")
    sys.exit()

search = raw_input("Please enter the tags to search for (in a comma separated list) or enter 'list' for list of existing tags : \n")

to_search = search.split(",")

if to_search == ["list"]:
    print(shelf.keys())
else:
    for term in to_search:
        if shelf.has_key(term):
            print(term + ":")
            for l in shelf[term]:
                print(l)
        else:
            print("No images found with this tag")


