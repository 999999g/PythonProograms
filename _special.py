import re
st = 'sdhgfsJGIOGH7846GHIFG8745726373jdcbjk1seyr+91-7854326538RGIOUR4785678GDSJKF8957VN905K'

data = re.findall('\+91-[6789][0-9]{9}',st)
print(data)