# Path = C:/Users/Karan/OneDrive/Documents/whitehatjr/python/C97/
# - Open the terminal 
# - Using cd command go to the folder which contains your conditionalAge.py file 
# - To run the file we use python3 filename command.
#  Here we'll write =====* python3 conditionalAge.py * ==== We'll see output on the terminal


age = int(input("Enter your age: "))
#Enter your age: 28  

if (age > 18): 
    print("You are an adult. You can vote!") 
elif (age > 12): 
    print("You are a teenager and a rebel!") 
else: 
    print("You are still a kid. There is so much in the world for you to see.")