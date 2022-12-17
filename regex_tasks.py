import re
import requests
import pandas as pd

import matplotlib.pyplot as plt
# %matplotlib inline

"""Задание №1"""

text1 = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references').text
data = re.findall(r'\b(ftp\..*)\b', text1)
links = []
for row in data:
    links += re.split(r'[\t;]', row)
links = list(set(links))

file = open("ftps.txt","w")
file.writelines('\n'.join(links))
file.close()

"""Задание №2"""

text2 = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD').text
nums = re.findall(r'[\d]+', text2)
print(*nums)

"""Задание №3"""

words_a = re.findall(r'\b(\w*[aA]\w*)\b', text2)
print(set(words_a))

"""Задание №4"""

sentances = re.findall(r'([A-Z][\s\w,]*!)', text2) 
print(sentances)

"""Задание №5"""

dist = []
for n in range(1, 16):
    dist += [n] * len(re.findall(r'\b[a-zA-Z]{' + str(n) + r'}\b', text2))

plt.hist(dist, bins=15)
plt.xlabel('Lenght')
plt.ylabel('Count')
plt.show()

"""Задание №6"""

def to_brick(text):
    return re.sub(r'([аеёиоуыэюя])', r'\1к\1',  text)

print(to_brick('молоко'))
print(to_brick('железо'))
print(to_brick('синхрофазатрон'))