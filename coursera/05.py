#!/usr/local/bin/python
import re
import json
import ssl

import urllib
from BeautifulSoup import *


import urllib
import xml.etree.ElementTree as ET



def get_sum_from_list(list):
        sum=0
        T2 = [int(column) for column in list] 
        for j in T2:
                sum=sum+j
        print  " j = %d" % (j) 
        return sum 

def str_to_int (str):
       return int(str)




serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location http://python-data.dr-chuck.net/comments_42.xml: ')
    if len(address) < 1 : break

#    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    url = address
 
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    counts = tree.findall('.//count')
    print "counts =  %d" % ( len(counts) ) 

    Sum=0
    i=0

    for i  in range(0 , len(counts)):  
	Sum=Sum+int (counts[i].text)		

    print "Sum: %d" %(Sum)

#    print counts[0].text 
     

#    results = tree.findall('result')
#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text

#    print 'lat',lat,'lng',lng
#    print location


