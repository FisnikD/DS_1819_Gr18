import re
import os
try:
    f = open("tekstFile.txt")
    if f.mode == 'r':
        contents = f.read()
except Exception as e:
    print e
    print "Please write the directory of the file you want to open"
    os.system("pause")
    exit()

def KeyFinder(contents,word):
    key = range(1,25)
    word = list(word)
    newWord = list()
    try:
        for i in key:
            for k in word:
                if k.isalpha():
                    j = (((ord(k)-97) + i) % 26) + 97
                    newWord.append(chr(j))
                else:
                    newWord.append(k)
            compText = ''.join(newWord)
            if re.search(" " + compText + " ",contents) != None:
                return i
            else:
                newWord = list()
    except:
        return None

def Decrypt(ciphertext,key):
    plaintext = list()
    for i in ciphertext:
        if i.isalpha():
            i = (((ord(i)-97) - key) % 26) + 97
            plaintext.append(chr(i))
        else:
            plaintext.append(i)

    plaintext = ''.join(plaintext)
    return plaintext

word = raw_input('Input the known word: ')

key = KeyFinder(contents,word)
if key != None:
    plaintext = Decrypt(contents,key)
else:
    plaintext = "Sorry, did not manage to decipher"
print plaintext