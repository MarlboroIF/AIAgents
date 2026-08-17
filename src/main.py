import snowflake.connector  #installed by ctr/alt/s/+/snowflake-connector-python
import boto3
import pandas as pd
import time
import os
from datetime import date
class Learn:
 gvarint=100
 gvarfloat=-25.9
 gvarstr='Learning Python'
 gvarbool= True
 gvarlong=10020
 gvarstr='String'
 gvarlist=['L1','L2','L3',1,2,3,5.4,-10]
 gvartuple=('T1','T2','T3','T4',1,3,5.7,-2.5,1+2j)
 gvardict={"Name":"Anupal", "Address":"Marlboro", "Name":"Sunita", "Address":"Moline"}
 gvarrange=range(5)
 var1=10
 var2=20
 varbool=None

 def myfunction(self):
  mylist=[]


if __name__ == '__main__':
        mylearn=Learn()
        a=int(1)
        b=int(2.2)
        c="3"
        print("Hello World Prgram")
        print(" gvarint value is {} ", mylearn.gvarint )
        print(" gvarint value is {} ".format(mylearn.gvarint))
        print(mylearn.var1==mylearn.var2)
        print("non Empty bool(mylearn.var1)",bool(mylearn.var1))
        print("varbool empty is=", bool(mylearn.varbool))
        print("gvarlong value is {}".format(mylearn.gvarlong))
        print("gvarfloat value is {}".format(mylearn.gvarfloat))
        print("gvarint value is {}".format(mylearn.gvarint))
        print("gvarstr value is {}".format(mylearn.gvarstr))
        print("gvarlist value is {}".format(mylearn.gvarlist))
        print("gvartuple value is {}".format(mylearn.gvartuple))
        print("gvardict value is {}".format(mylearn.gvardict))
        print("gvarrange value is {}".format(mylearn.gvarrange))

        if ( mylearn.var1 == mylearn.var2 ):
            print ("Value of expression is 100")
        print ("Good bye!")


        for letter in 'Python':  # First Example
            if letter == 'h':
                break
            print ('Current Letter :', letter)

        var = 10  # Second Example
        while var > 0:
            print ('Current variable value :', var)
            var = var - 1
            if var == 5:
                break

        print ("Good bye!")

        i = 2
        while (i < 100):
            j = 2
            while (j <= (i / j)):
                if not (i % j):
                    break
                j = j + 1

            if (j > i / j):
                print (i," is prime")
            i = i + 1

        print ("Good bye!")

        var1 = 'Hello World!'
        var2 = "Python Programming"

        print ("var1[0]: ", var1[0])
        print ("var2[1:5]: ", var2[1:5])

        var1 = 'Hello World!'
        print ("Updated String :- ", var1[:6] + 'Python')
        print("new var1 :- ", var1)

        print ("My name is %s and weight is %d kg!" % ('Zara', 21))

        import time;

        localtime = time.localtime(time.time())
        print ("Local current time :", localtime)
        print("Today date is {}".format(date.today()))
        try:
            print("The date is {}".format(date.today()))
        except Exception as ex:
            print("The error is ", ex)
            exit()
        finally:
            print("This is finally")

def printme(str):
    #"This prints a passed string into this function"
    print(str)
    return
class Person:

 def __init__(self, name, age):
        self.name = name
        self.age = age

        if isinstance(age , str):
            self.name = name + " " + age


 def __str__(self):
        return f"{self.name}({self.age})"

 def myfunc(self):
        print("Hello my name is " + self.name)

 def printname(self):
        print("The Student name is "+self.name)

class Student(Person):
  pass

p1 = Person("John", 36)
p1.myfunc()
x = Student("Mike", "Olsen")
x.printname()
#str2 = input("Enter your input: ")
#print ("Received input is : ", str2)
fo = open("C:\\Users\\anupa\\OneDrive\\Pictures\\Documents\\Mongo query.txt", "w+")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
#print ("Softspace flag : ", fo.softspace)
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()
fo = open("C:\\Users\\anupa\\OneDrive\\Pictures\\Documents\\Mongo query.txt", "r+")
str1 = fo.read(100);
print("Read String is : ", str1)
position = fo.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str2 = fo.read(10)
print ("Again read String is : ", str2)
fo.close()
import smtplib
import base64
import socket

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   #smtpObj = smtplib.SMTP('localhost')
   smtpObj=smtplib.SMTP('mail.your-domain.com', 25)
   encodedcontent = base64.b64encode(str1)  # base64
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except Exception as ex:
   print ("Error: unable to send email", ex)