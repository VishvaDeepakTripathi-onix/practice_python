##############################################
#   idea is to read the files form given dir.
#   Cases are followings
#       1. No files in DIR
#       2. 0 KB files are in DIR
#       3. Files already processes
#       4. Not processed.
#
##############################################
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)
# p1.myfunc()



class filechecker:
  def __init__(self,FilePath):
    self.FilePath = FilePath

  #this function need to read the files and open it.
  def __FileChecker__(self):
    # File in open mode
    filePath = self.FilePath
    fOpen = open(filePath, "rt")
    print(fOpen.read())

# Creating the object of the classs
objFilechecker = filechecker("InputFiles/input.txt")
# Calling function of the class through object.
objFilechecker.__FileChecker__()
