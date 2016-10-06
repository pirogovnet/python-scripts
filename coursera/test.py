#!/usr/local/bin/python
import getpass
import sys
import telnetlib
import csv
import random
import math



def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
        return max_of_2(a, max_of_2(b, c)) 


m3=0
m5=0
for i in xrange (1,100):
        if (i % 3 ==0): 
              m3=1;
        if (i % 5==0): 
              m5=1;

        if (m3==1 and  m5==1):
                print '%d MOD3 an MOD5\n' % (i) 
        elif (m3):
               print '%d MOD3 \n' % (i)
        elif  (m5):
               print '%d MOD5 \n' % (i) 


        m3=m5=0 


count=0;
resstr="";

str1="aaavvvbbbbddddrrrrrggggaaaaa"

for i in range(len(str1) -1 ):
#      print str[i]

       if(str1[i] == str1[i+1]): 
         count=count+1
#         print 'count =%d\n' %(count)

       else:
         d2=str(count)  
         resstr+=str1[i]+ d2 
         count=0 

print 'result string == %s ' % (resstr)
         
