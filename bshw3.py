from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
import re
import ast
import json

# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
#


#############################################################################################
myname = "Name: Thomas Kidd "
section = "Section Day/Time: 002 Wednesday 5:30-6:30 "
id_number = 'UMID Number: 85828979'

print (myname +'\n' +section +'\n'+ id_number)
#############################################################################################

atxt_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'

y = requests.get(atxt_url)

soup = BeautifulSoup(y.text, 'lxml')

print ("## PART 1 ##")
#print (type(soup.text))

getAllStudents = soup.find_all(text=re.compile('student'))
for each in getAllStudents:
	newsoup = str(each).replace('student',"AMAZING student")
	each.replace_with(newsoup)

print ("## PART 2 ##")

for imageLink in soup.findAll('iframe'):
	imageLink['src'] = "/Users/tommykidd/tom_alex.png"

print ("## PART 3 ##")

for imageLink in soup.findAll('img'):
	imageLink['src']='/Users/tommykidd/Desktop/206/SI206-master/HW3-StudentCopy/media/logo.png'

f = open('bshw3textout.html','w')
f.write(str(soup))
f.close()

#############################################################################################

#print (soup)
#print (type(soup))

# mess = soup.text.split(" ")

# #print ((mess))
# print ("gggggggddddddjhaksjdhlfkjsdhfkahsdkjfahsdkjfhakjdshfkaljsdhlf")
# studOptions = ['student','students','Student','Students']
# def souper(x):
# 	for word in x:
# 		for y in studOptions:
# 			if y == word:
# 				x[mess.index(word)]=("AMAZING "+y+"")
# 	#print(x)
# 	return x

# 	#print (x)
# print(type(souper(mess)))
# theString = ""
# for t in souper(mess):
# 	theString+=(t+" ")




# theHtml=bs(theString)                #make BeautifulSoup
# prettyHTML=theHtml.prettify()

# print(prettyHTML)


# f = open('bshw3textout2','w')
# f.write(prettyHTML)
# f.close()

