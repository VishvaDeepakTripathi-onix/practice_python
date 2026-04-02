# This will look into file and perform the following steps 
# 1. Check the new file availability. 
# 2. File Size >0KB
# 3. file is not already processed. 
import os

class FileLooker:
  def __init__(self,FilePath):
    self.FilePath = FilePath
    self.fSize =0

  #this function need to read the files and open it.
  #check for the availability and updated files 
  def __FileChecker__(self):
    # File in open mode
    filePath = self.FilePath
    fOpen = open(filePath, "rt")
    print(fOpen.read())
  
  #FileSize need to be checked. 
  def __FileSize__(self):
    # File in open mode
    filePath = self.FilePath
    fSize = os.path.getsize(filePath)
    #print(fSize.read())
    return fSize

# Creating the object of the classs
objFilechecker = FileLooker("input\inputfiles.sql")
# Calling function of the class through object.
objFilechecker.__FileChecker__()
x=objFilechecker.__FileSize__()
if x <0 :
    print("File size is 0 KB")
else :
    print("Actual file size {}" .format(x) )