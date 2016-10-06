#!/usr/local/bin/python
import getpass
import sys
import telnetlib
import csv

user = "test"
password = "test"

router = "[local]ssr8010#"

tn = telnetlib.Telnet()
tn.open("1.1.1.1s")
tn.read_until("login: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.read_until(router)
#tn.write("context Signaling \n")
#print tn.read_until(router)
tn.write("show subs summ all | grep CLIPs\n")
output = tn.read_until(router)
tn.write("exit\n")
tn.read_all()
print output.split()[9]
tn.close()
