# declare two variables wordCount and characterCount in our program. #
# The 'characterCount' variable is initialized to zero and the wordCount variable is initialized to 1. #
#characterCount=0 
#wordCount=1 
# use a for loop to iterate on the string. To do that we'll write 
#for character in introString:
#here "character" is the loop variable 
# # which will be assigned list elements from introString one after the other 
# # (including space). The for loop is used to traverse through the characters in the string 
introString = input("Enter your introduction:") 
characterCount = 0 
wordCount = 1 
# Inside the for loop to count the character we'll write :- 
# # (To write the statement or code inside a function we will add an indentation at the beginning) 
# # (The character count is incremented each time a character is encountered). 
for i in introString: 
    characterCount = characterCount + 1 
    if(i == ' '): 
        wordCount = wordCount+1 
        # We'll check for the blank space in between the words. 
        # While iterating on the introString "character" also takes all the blank spaces it contains. 
        # So whenever "character" encounters # a blank space we'll mark it as a word and increase the word count. 
        # # The code for this would be: if(character == ' '): wordCount=wordCount+1 
        # # Note the user does not press space after the last word. 
        # This needs to be kept in account when printing the final wordCount, the final wordCount has # to be increased by 1. 
print("Number of words in the string:") 
print(wordCount + 1) 
print("Number of characters in the string:") 
print(characterCount)