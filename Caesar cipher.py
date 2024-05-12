def encode(s, d):
    # I create the translation table with the maketrans function for encoding.
    mapping = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", #The first argument is a string, which will be translated.
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[d:] + #The syntax [d:] takes the first string from element d.
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[:d]  #And syntax [:d] takes first string to the element d.
        #The second argument is a 'moved string'.
        # We map each letter in the alphabet to its corresponding shifted letter.
    )
    #I use the translate method to return a string where specified characters are replaced with the characters described in a mapping table.
    encoded_string = s.translate(mapping)
    return encoded_string
    #The function returns an encoded string.
def decode(s, d):
    # I create the translation table with the maketrans function for decoding.
    mapping = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", #The first argument is a string, which will be translated.
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[-d:] + #The syntax [d:] takes the first string from element d.
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[:-d] #And syntax [:-d] takes first string to the element d.
        #The second argument is a 'moved string'.
        # We map each letter in the alphabet to its corresponding shifted letter.
    )
     #I use the translate method to return a string where specified characters are replaced with the characters described in a mapping table.
    decoded_string = s.translate(mapping)
    return decoded_string
    #The function returns a decoded string.
string = input("Enter the word to encode or decode: ") # I take the word from user.
shift = int(input("Enter the shift parameter (positive integer): ")) # I take shift parameter from user.
shift %= 26 #If the shift is bigger than 26 then the rest of the division is the result.
choice = input("Enter 'encode' to encode or 'decode' to decode: ") #The user chooses between encoding or decoding

if choice == 'encode': #If the choice of the user is encoded then I call the function encode.
    result = encode(string, shift) #This function 'encode' takes two parameters: string and shift, which are input from the user.
    print("Encoded string:", result)
elif choice == 'decode': #If the choice of the user is decode then I call the function decode.
    result = decode(string, shift) #This function 'decode' takes two parameters: string and shift, which are input from the user.
    print("Decoded string:", result)
else:
     print("Invalid choice.") 
     #If the user inputs the wrong choice, the program returns the proper comment.