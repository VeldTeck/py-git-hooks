import sys
import os

from os import path

hookT = ".git/hooks/" + sys.argv[1]

fileExists = False

if path.exists(hookT):
    fileExists = True
else:
    print (sys.argv[1] + " is not a pre-existing hook\n")

f = open(hookT, "a+")
f2 = open(hookT, "r")

f3 = f2.read()

commandExists = False

packMan = None

if not fileExists:
    print ("creating it\n")
    f.write("#!/bin/bash")

if path.exists("pom.xml"):
    print ("trying to insert maven command\n")
    packMan = "mvn"
elif path.exists("build.gradle"):
    print ("trying to insert gradle command\n")
    packMan = "gradle"

if (packMan + " " + sys.argv[2]) not in f3:
    print ("creating new command \"" + packMan + " " + sys.argv[2] + "\"\n")
    f.write("\n")
    f.write(packMan + " " + sys.argv[2])
else:
    print ("\"" + packMan + " " + sys.argv[2] + "\" already exists as a " + sys.argv[1] + " hook")

f.close()
f2.close()