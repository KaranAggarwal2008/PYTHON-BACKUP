#This program is for custom built functions in python
#This function will access file given by the user and return number of words in the file

#The function definition follows from line number 4 to 17
def countWordsFromFile():
    fileName = input("Enter The File Name(Path):- ")

    numberOfWords = 0
    numberOfLines = 0

    fileObject = open(fileName, 'r')

    for eachLine in fileObject:
        #Count the number of lines
        numberOfLines = numberOfLines + 1
        #Count the number of words
        listOfWords = eachLine.split()
        numberOfWords = numberOfWords + len(listOfWords)

    #Print the number of lines
    print("Number Of Lines in the given file: ")
    print(numberOfLines)

    #Print the number of words
    print("Number Of Words in the given file: ")
    print(numberOfWords)

#This is function calls
countWordsFromFile()