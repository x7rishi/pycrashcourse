#!/usr/bin/python3
with open("allo/poo.txt") as file_obj:
    content = file_obj.read()
    print(content.rstrip())
    print("length of the document will be ",len(content))