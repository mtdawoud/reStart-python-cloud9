{"filter":false,"title":"debug-caesar-1.py","tooltip":"/debug-caesar-1.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #1","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + cipherKey","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, decryptKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":2}],[{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"insert","lines":["i"],"id":3},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"insert","lines":["n"]},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"insert","lines":["("],"id":4}],[{"start":{"row":27,"column":34},"end":{"row":27,"column":35},"action":"insert","lines":[")"],"id":5}],[{"start":{"row":27,"column":38},"end":{"row":27,"column":39},"action":"insert","lines":["i"],"id":6},{"start":{"row":27,"column":39},"end":{"row":27,"column":40},"action":"insert","lines":["n"]},{"start":{"row":27,"column":40},"end":{"row":27,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":41},"end":{"row":27,"column":42},"action":"insert","lines":["("],"id":7}],[{"start":{"row":27,"column":51},"end":{"row":27,"column":52},"action":"insert","lines":[")"],"id":8}],[{"start":{"row":27,"column":25},"end":{"row":27,"column":26},"action":"remove","lines":["("],"id":9},{"start":{"row":27,"column":24},"end":{"row":27,"column":25},"action":"remove","lines":["t"]},{"start":{"row":27,"column":23},"end":{"row":27,"column":24},"action":"remove","lines":["n"]},{"start":{"row":27,"column":22},"end":{"row":27,"column":23},"action":"remove","lines":["i"]}],[{"start":{"row":27,"column":30},"end":{"row":27,"column":31},"action":"remove","lines":[")"],"id":10}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":0},"end":{"row":4,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":16,"state":"start","mode":"ace/mode/python"}},"hash":"784b51fb871369e13629689d31afef974e3daef1","mime":"text/x-script.python","timestamp":1670494732535}