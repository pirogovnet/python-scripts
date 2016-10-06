#!/usr/local/bin/python
import re
import json
import ssl

import urllib
from BeautifulSoup import *


def get_sum_from_list(list):
        sum=0
        T2 = [int(column) for column in list] 
        for j in T2:
                sum=sum+j
        print  " j = %d" % (j) 
        return sum 

def str_to_int (str):
       return int(str)




url = raw_input('Enter - ')
count= int (raw_input('count - '))
position  = int (raw_input('position - '))

print 'Retrieving', url
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
html = uh.read()

#html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags

i=0
j=0


for i in range(0, count ):
        print i	
	tags = soup('a')

#for tag in tags:
#    print tag.get('href', None)
    
	print tags[position-1].get('href', None)
	 
	next_url=tags[position-1].get('href', None)

 
	print 'Retrieving j=1', next_url
	scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	uh = urllib.urlopen(next_url, context=scontext)
	html = uh.read()
        soup = BeautifulSoup(html)
        tags = soup('a')
	 
