#!/usr/local/bin/python
import re


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
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

Count=0
Sum=0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag

    if (int (tag.contents[0]))>0:
	Count=Count+1		
    
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    Sum=Sum+str_to_int(tag.contents[0])
    print 'Attrs:',tag.attrs

    print "Count = %d \n" % (Count)
    print "Sum= %d \n" % (Sum)

		
	 

