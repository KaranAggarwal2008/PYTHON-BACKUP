# Path = C:/Users/Karan/OneDrive/Documents/whitehatjr/python/C98/projectPost/
# - Open the terminal 
# - Using cd command go to the folder which contains your swappingFile.py file 
# - To run the file we use python3 filename command.
#  Here we'll write =====* python3 swappingFile.py * ==== We'll see output on the terminal
def swappingFile(file1, file2):
    #Swapping File Started
    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1,'w') as c:
        c.write(data_b)

    with open(file2, 'w') as d:
        d.write(data_a)
    print("Swapped files succesfully please check Thanks for using")


def inputBoxForSwap():
    file1Path = input("Please enter the name of you first file(Path):- ")
    file2Path = input("Please enter the name of your second file(Path):- ")
    swappingFile(file1Path, file2Path)
    print("Swapping files")

inputBoxForSwap()
