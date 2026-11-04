""" get unique ip id fromthe log the request
get how many 200,300,400 error code in log File
write the result to csv File """

""" import os

joining the path
path ="C:\\Users\\Admin\\Desktop\\mini project"
myfile="mylog.txt"
print(os.path.join(path,myfile)) """

#read the file
""" with open(os.path.join(path,myfile))as file:
    content =file.read()
    print(content[:100]) """

# print whole and each data
""" with open(os.path.join(path,myfile))as file:
    for each in file:
        print(each)
        break """

import os
import csv
ip=[]
http_status=[]


#joining the path
path ="C:\\Users\\Admin\\Desktop\\python project"
myfile="mylog.log"
print(os.path.join(path,myfile))

#split the value
""" with open(os.path.join(path,myfile))as file:
    for each in file:
        print(each.split(" "))  #split the value(string) and store in list
        break """

# print ip and status code
with open(os.path.join(path,myfile))as file:
    for each in file:
        mylist =each.split(" ")

        # ip.append(mylist[3])   
        # print(ip)     

        http_status.append(mylist[8])
        print(http_status)

# frequency
mydict={}
def frequency(mylist):    
    for each in mylist:
        if each not in mydict:
            mydict[each]=1
        else:
            mydict[each]+=1
    return mydict

# create and write csv file
def write_to_csv(mydict):
    with open(os.path.join(path,"new_csv.csv"),"w",newline = "")as f:
        writer = csv.writer(f)
        writer.writerow(["Sno","http_status","Frequncy"])
        Sno = 1
        for each in mydict:
            writer.writerow([Sno,each,mydict[each]])
            Sno +=1
rest1 = frequency(ip)
rest2 = frequency(http_status )

write_to_csv(rest1)
write_to_csv(rest2)

print("CSV file created successfully")
           

       





