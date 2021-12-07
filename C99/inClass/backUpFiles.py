#Import os and shutil to use later
import os
import shutil 

#Request the source and destination input
source = input("enter source folder name:- ") 
destination = input('enter destination folder name:- ') 

#Add / in the end
source = source + '/' 
destination = destination + '/' 

#Copy all files in destination
list_of_files = os.listdir(source) 
for file in list_of_files: 
    shutil.copy((source+file), destination)