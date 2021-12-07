# -- Reading and writing files doc -- https://www.geeksforgeeks.org/reading-writing-text-files-python/ 
# -- Split method doc -- https://www.geeksforgeeks.org/python-string-split/ 

1. Create a file called "test.txt" 
2. Open python console. Use f = open("test.txt") to store the file in 'f' variable. 
3. Use f.read() to read the file and then prints it on the console. 
# - By default a file opens in read mode. 
# We could have also used open("test.txt",'r') to open the file explicitly in the read mode.
# - file is an object in python which has several functions defined on them. 
# read() is a function defined on files. 
# - "\n" represents the Enter or return key 
# -- You can also print a file line by line in python. 
# open() function can be used to open any file in read, write or append mode. 
# The function returns a file object which we can read in our program. f = open("test.txt") fileLines = f.readlines() 
# readlines() defined on file object splits the lines in the file and stores it line by #line as a list. We can print these lines by calling a for loop on the list. for line in fileLines: print(line) 
# There are several other functions defined on files which you can explore # on your own by referring to the documentation. 
# A FILE IS AN OBJECT IN PYTHON 
# For example - a variable which holds a string is also an object in python. # Let's store a string inside a variable. 

    introString = "My name is Wily, I am 15 years old." 

# introString is a string object on which several functions are defined. One of the functions defined on introString is called split(). 
# split() splits the given string by their whitespaces, gives each individual word and stores them in a list. We can write: 

    words = introString.split() 
    print( words ) 

# split() splits using whitespace by default. You can also specify which separator to use to split the items. 
# For example, we could have used comma (,) as the separator: 

    phrases = introString.split(",") 

- Again, there are several functions defined on string object in Python. 
- You can look over them in the documentation for python. 
- Now, we have used several functions which are pre-defined in python. Let's learn how to define a custom 
- function in python. You already know how to define a custom function in javascript. 
- It is similar in python except for the change in syntax. 
- To define a function in python, we use the syntax: 

    def functionName(): 
        <block of code for the function> 

- You can also pass arguments to your function inside the brackets 
- similar to how we did in javascript. 

    def functionName(variable):
        <block of code for the function> 

 # There are a lot of places where there is a restriction on the number of words to be used 
 - for example while writing essays....we can use the program to count the number of words used. 
 # creating a countWordsFromFile.py file. Inside the file, let's create a custom function countWordsFromFile() which takes the file path as input. We can open the file using open() in read mode. 
 # We can read all the lines in our file and store it in a list. For each line in the file, let's split the line by whitespace to store all the words in the line as a list. 
# For each line in the file, you can use split() to split the line by whitespace and store the words in the words list 
# We use a numberOfWords variable which starts from 0 We count the number of words in the words list for each file and keep adding to the numberOfWords 
# There is a predefined function len() in python which will give you the length of the list. We can use it to find the length of words listed for each line. 

    numberOfWords =0 
    numberOfWords = numberOfWords + len(words) 

# - to increment the value of count by the number of words in each line of the file.