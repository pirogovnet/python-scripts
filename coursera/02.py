#!/usr/local/bin/python
import re


def get_sum_from_list(list):
#       for i in list:
        sum=0
#        T2 = [(int, x) for x in list]
#       T2 = [[int(column) for column in row] for row in T1]
        T2 = [int(column) for column in list] 

        for j in T2:
                sum=sum+j
        print  " j = %d" % (j) 
        return sum 


count=0
summ=0

#file = open ('02-test.txt')
file = open ('02-to-do.txt')

for line in file:
        line=line.rstrip()
#       number=re.search([0-9]+)
        number =re.findall('([0-9]+)',line)

        if len(number)>0: 
                print number
                count=count+len(number)
                summ=summ+get_sum_from_list(number)


print "wors count = %d , summa = %d" % (count,summ)
