import os
cwd= os.getcwd()
print(cwd)

new= os.path.abspath("my_story.txt")
print(new)

os.chdir(r"C:\Users\iguthriebeckstrom01\Desktop\q1")
fout= os.getcwd()
print(fout)

name=os.listdir()
print(name)
