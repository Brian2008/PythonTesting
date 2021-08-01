intro=input("Enter your Introduction->")
charaterCount=0
wordCount=1
for i in intro:
    charaterCount=charaterCount+1
    if(i==' '):
        wordCount=wordCount+1
print("number of words in the string are ")
print(wordCount)        
print("number of charaters in the string are ")
print(charaterCount)     

