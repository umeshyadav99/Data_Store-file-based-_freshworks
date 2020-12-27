#run the MODULE of MAIN FILE and import mainfile as a library 

import source_code as d #importing the main file("source_code" is the name of the file I have used) as a library 


d.create("Apple",25) #to create a key with key_name,value given and with no time-to-live property


d.create("Samsung",70,3600) #to create a key with key_name,value given and with time-to-live property value given(number of seconds)


d.read("Apple") #it returns the value of the respective key in Jasonobject format 'key_name:value'

d.read("Samsung") #it returns the value of the respective key in Jasonobject format 'key_name:value'

d.read("Apple") #it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

d.create("Apple",50) #it returns an ERROR since the key_name already exists in the database 

d.delete("Apple") #it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
th1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
th1.start()
th1.sleep()
th2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
th2.start()
th2.sleep()
#this can be accesed upto thn
