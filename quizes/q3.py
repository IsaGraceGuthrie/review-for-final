#move the text file to a  new folder in side the folder
# list the documents in teh folder


import os

os.mkdir("documents")

cwd=os.rename("text.txt","documents/text.txt")

fout=os.listdir()
print(fout)
