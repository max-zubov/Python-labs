#!/usr/bin/python

# script for find a polindrom

#test = "арозаупаланалапуазора"
#test = "What is it?"
#test = ""
test = str(input())

if test == test[::-1]:    print("String '" + test + "' is polindrom.")
else:                     print("String '" + test + "' is not polindrom.")
