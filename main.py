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

def create(key,value,timeout=-1):#initial timeout -1 means infinite time 
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
                with open('data.txt', 'w') as outfile:
                    json.dump(data, outfile)
            else:
                print("error: Memory limit exceeded!! ")#error
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error 
