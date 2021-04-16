scramble = input("Enter the scrambled anagram: ")
scrambleLength = len(scramble)
wordList = open("words_alpha.txt") # list of english words
matches = 0

for word in wordList:
    success = 0
    wordClean = word.strip()
    wordLength = len(wordClean)
    
    
    if (wordLength == scrambleLength): #only proceed if overall length matches
        
        success = 0
                
        for letter in scramble:
            
                
                
                if (letter in word):

                    letterCount = scramble.count(letter) #count instances of this letter to make sure it matches the count of the dictionary word
                    letterCount2 = word.count(letter)
                    if (letterCount != letterCount2):
                        success = 0
                    
                    success = success + 1
                    if (success == wordLength):
                        print(word)
                        matches = matches + 1
                else:
                    success = 0
                    break
if matches < 1:
    print("No English matches found.")

                    

