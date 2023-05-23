import os
import shutil
from_dir=os.listdir("C:/Users/Administrator/Desktop/abcdef")
to_dir=os.listdir("C:/Users/Administrator/Downloads")
list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
  root,ext=os.path.splitext(i)
  print("the root of the file is",root)
  print("the ext of the file is",ext)
