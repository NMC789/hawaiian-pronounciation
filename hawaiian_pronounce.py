consonants = ["h", "w", "p", "k", "l", "m", "n"]
vowels = {"a":"ah", "e":"eh", "i":"ee", "o":"oh", "u":"oo"}
doubleVows = {"ai":"eye", "ae":"eye", "ao":"ow", "au":"ow", "ei":"ay", "eu":"eh-oo", "iu":"ew", "oi":"oyo", "ou":"ow", "ui":"ooey"}

"keiki -> kay-kee X Kay-ee-kee"

def validate(word):
    """
    Checks if word has only valid letter in it.
    Assumes word is string.
    returns true if valid hawaiian word, false if otherwise
    """
    word = word.lower()
    counter = 0
    for letter in range(len(word)):
        
        if word[letter] in "aeiouhwpklmn '":
            counter += 1
        else:
            invalid = word[letter]
            
    if counter == len(word):
        return True
    else:
        return False
        

def pronounce(word):
    """
    Given a valid hawaiian word,
    returns a string that gives the correct pronunciation
    """
    word = word.lower()
    output = ""
    index = 0
    while index < len(word):
        #if letter at index and next letter is a double vowel, handle
        if word[index:index + 2] in doubleVows:
            output += doubleVows[word[index:index+2]]
            index += 2
            
        #if letter at index is a vowel, handle
        elif word[index] in vowels:
            output += vowels[word[index]]
            index += 1
            
        #if letter is consonant, handle that
        elif word[index] in consonants:
            if word[index] == "w":
                if index == 0:
                    output += "w"
                    
                elif word[index - 1] == "i" or word[index - 1] == "e":
                    output += "v"
                    
                elif word[index - 1] == "u" or word[index - 1] == "o":
                    output += "w"
                index += 1
            else:
                output += word[index]
                index += 1

        #If apostrophe, handle that
        elif word[index] == "'":
            output = output.strip("-")
            output += "'"
            index += 1
            
        if index >= len(word) or word[index-1] == "'" or word[index-1] == " " or word[index-1] in consonants:
            output += ""
            
        else:
            output += "-"

    return output.capitalize()

while True:
    word = input("Enter a Hawaiian word to pronounce: ")
    if validate(word) == True:
        hawaii_pro = pronounce(word)
        print(word.upper(), "is pronounced", hawaii_pro)
        exit_key = input("Do you want to enter another word? y/YES n/NO ==> ")
        if exit_key == "n":
            break   
    else:
        print("This is not a valid Hawaiian character.")


