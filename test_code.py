#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import main as data 
#importing the main file("code" is the name of the file I have used) as a library 
import threading 
from threading import*

data.create("nikhil",25)
#to create a key with key_name,value given and with no time-to-live property


data.create("good",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


data.read("nikhil")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


data.read("good")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


data.create("nikhil",50)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 

#or use delete operation and recreate it
 
data.delete("nikhil")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
try:
   thread.start_new_thread( data.create, ("Thread-1", 2) )
   thread.start_new_thread( data.create, ("Thread-2", 4) )
except:
   print("Error: unable to start thread")
#and so on upto tn

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB