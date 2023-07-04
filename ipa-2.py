'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import string
    alphabet=list(string.ascii_uppercase)
    letter=letter.upper()

    if letter==" ":
        return (" ")
    else:
        move=alphabet[alphabet.index(letter)+shift-(26*(shift//26+1))]
        return move

shift_letter("h",5)


def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import string
    alphabet=list(string.ascii_uppercase)
    message=message.upper()
    start=""


    for letter in message:
        if letter==" ":
            move=" "
            start=start+move
        else:
            move=alphabet[alphabet.index(letter)+shift-(26*(shift//26+1))]
            start=start+move

    return start

caesar_cipher("happy",7)


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import string
    alphabet=list(string.ascii_uppercase)
    letter=letter.upper()
    letter_shift=letter_shift.upper()

    if letter==" ":
        return (" ")
    else:
        if alphabet.index(letter)+alphabet.index(letter_shift)<26: 
            move=alphabet[alphabet.index(letter)+alphabet.index(letter_shift)]
        else: #wrap beyond Z
            move=alphabet[alphabet.index(letter)+alphabet.index(letter_shift)-26]
        return move

shift_by_letter("j","f")


def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import string
    alphabet=list(string.ascii_uppercase)
    message=message.upper()
    key=key.upper()

    #number value of key
    ko_list=list()

    if len(key)==len(message):
        for letter2 in key:
            key_order=alphabet.index(letter2)
            ko_list.append(key_order)
    else:
        keyrepeat=len(message)//len(key) 

        if len(message)%len(key)==0: #complete repetition of key
            newkey=(key*keyrepeat)
        else: # repetition of key with extra letters
            newkey=(key*keyrepeat)+key[0:len(message)-(len(key)*keyrepeat)]
        for letter2 in newkey:
                key_order=alphabet.index(letter2)
                ko_list.append(key_order)
    
    #start of encryption
    new_start=""

    for letter,ko in zip(message,ko_list):
        if letter==" ":
            move=" "
            new_start=new_start+move
        else:
            if alphabet.index(letter)+ko<26:
                move=alphabet[alphabet.index(letter)+ko]
                new_start=new_start+move
            else:
                move=alphabet[alphabet.index(letter)+ko-26]
                new_start=new_start+move
    return new_start

vigenere_cipher("seven teen","carat")


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    message=message.upper()

    #check if complete shift repetition
    if len(message)%shift==0:
        new_message=message
    else:
        new_message=message+"_"
        while len(new_message)%shift!=0:
            if len(new_message)%shift==0:
                break
            else:
                new_message=new_message+"_"
    
    #rearranging letters for encryption
    new_start=""

    for x in range(0,len(new_message)):
        new_start=new_start+new_message[(x//shift)+(len(new_message)//shift)*(x%shift)]
        #gets letter after each shift cycle
            #(1) cycle & letter per cycle count
            #(2) letters position in each cycle
                #shifts * letters position per cycle

    return new_start

scytale_cipher("happy_birthday",5)


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    message=message.upper()
    old_start=""

    for x in range(0,len(message)):
        old_start=old_start+message[(x//(len(message)//shift))+(shift*(x%(len(message)//shift)))]
        #(1) cycle & letters per cycle count
        #(2) letters position in each cycle
            #shifts * letters position per cycle
    
    return old_start

scytale_decipher("HPBTAAYIHYP_RD_",5)
