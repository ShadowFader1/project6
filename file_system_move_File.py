import os

srcpath = "name.txt"
despath = "AboutMe.txt"

os.rename(srcpath,despath)

print("The file is now renamed!")