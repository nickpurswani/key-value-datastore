#this is to make key-value data store using python3
#for freshworks problem statement
#code begins 
#--------------------------------------------------
import threading 
from threading import*
import time
import json

data={} #dictionary to store data
#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is in seconds
def create(key,value,timeout=0):#initial timeout 0 means infinite time 
    if key in data:
        print("error: this key already exists") #error
    else:
        if(key.isalpha()):
            if len(data)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: # key_name capped at 32chars
                    data[key] = l
                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile)
            else:
                print("error: Memory limit exceeded!! ")#error
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error 
#for read operation
#use syntax "read(key_name)"
            
def read(key):
    try:
        fo = open("data.json", "r")
        data = json.load(fo)
        print(data)
        pass
        fo.close()
    except IOError:
        data = {}
    if key not in data:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=data[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri
