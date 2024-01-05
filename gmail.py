import re
st = 'comausdoas7DS9Duad7SUgayi123@gmail.comDOIAID7e38u8sd8yuw7d928eHT5RU6'
data = re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail\.com',st)
print(data)