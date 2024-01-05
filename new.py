import re

with open(r"C:\Users\Adminstrator\Desktop\content.txt",'r+') as file:
      data = file.read()
      data1= re.sub('a','@',data)
      file.write(data1)
      