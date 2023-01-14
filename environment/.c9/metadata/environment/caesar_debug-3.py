{"filter":false,"title":"caesar_debug-3.py","tooltip":"/caesar_debug-3.py","ace":{"folds":[],"scrolltop":498,"scrollleft":0,"selection":{"start":{"row":20,"column":17},"end":{"row":20,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":29,"state":"start","mode":"ace/mode/python"}},"hash":"1e5877ccda1f777987ccdb104790f9bd0b887819","mime":"text/x-script.python","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":55,"column":24},"action":"insert","lines":["# Module Lab: Caesar Cipher Program Bug #3","#","# In a previous lab, you created a Caesar cipher program. This version of","# the program is buggy. Use a debugger to find the bug and fix it.","","# Double the given alphabet","def getDoubleAlphabet(alphabet):","    doubleAlphabet = alphabet + alphabet","    return doubleAlphabet","","# Get a message to encrypt","def getMessage():","    stringToEncrypt = input(\"Please enter a message to encrypt: \")","    return stringToEncrypt","","# Get a cipher key","def getCipherKey():","    shiftAmount = input(\"Please enter a key (whole number from 1-25): \")","    return shiftAmount","","# Encrypt message","def encryptMessage(message, cipherKey, alphabet):","    encryptedMessage = \"\"","    uppercaseMessage = \"\"","    uppercaseMessage = message.upper()","    for currentCharacter in uppercaseMessage:","        position = alphabet.find(currentCharacter)","        newPosition = position + int(cipherKey)","        if currentCharacter in alphabet:","            encryptedMessage = encryptedMessage + alphabet[newPosition]","        else:","            encryptedMessage = encryptedMessage + currentCharacter","    return encryptedMessage","","# Decrypt message","def decryptMessage(message, cipherKey, alphabet):","    decryptKey = -1 * int(cipherKey)","    return encryptMessage(message, cipherKey, alphabet)","","# Main program logic","def runCaesarCipherProgram():","    myAlphabet=\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\"","    print(f'Alphabet: {myAlphabet}')","    myAlphabet2 = getDoubleAlphabet(myAlphabet)","    print(f'Alphabet2: {myAlphabet2}')","    myMessage = getMessage()","    print(myMessage)","    myCipherKey = getCipherKey()","    print(myCipherKey)","    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)","    print(f'Encrypted Message: {myEncryptedMessage}')","    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)","    print(f'Decrypted Message: {myDecryptedMessage}')","","# Main logic","runCaesarCipherProgram()"],"id":2}],[{"start":{"row":37,"column":35},"end":{"row":37,"column":44},"action":"remove","lines":["cipherKey"],"id":3},{"start":{"row":37,"column":35},"end":{"row":37,"column":36},"action":"insert","lines":["d"]},{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["e"]},{"start":{"row":37,"column":37},"end":{"row":37,"column":38},"action":"insert","lines":["c"]},{"start":{"row":37,"column":38},"end":{"row":37,"column":39},"action":"insert","lines":["r"]},{"start":{"row":37,"column":39},"end":{"row":37,"column":40},"action":"insert","lines":["y"]},{"start":{"row":37,"column":40},"end":{"row":37,"column":41},"action":"insert","lines":["p"]},{"start":{"row":37,"column":41},"end":{"row":37,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":37,"column":42},"end":{"row":37,"column":43},"action":"insert","lines":["K"],"id":4},{"start":{"row":37,"column":43},"end":{"row":37,"column":44},"action":"insert","lines":["e"]},{"start":{"row":37,"column":44},"end":{"row":37,"column":45},"action":"insert","lines":["y"]}]]},"timestamp":1670494737743}