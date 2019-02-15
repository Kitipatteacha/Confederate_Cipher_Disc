text = input("input text : ").strip().lower()
key = input("input key : ").strip().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
encryptedword = ""
keyToIndex = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7,
     "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,
     "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24,
     "z":25}
count = 0
VTable =[["" for x in range(26)] for y in range(len(key))]
for i in range (len(key)):
     for j in range (26) :
         a = keyToIndex[key[i]]
         VTable[i][j] = (alphabet[(j + a)%26])
for i in text:
    Vindex = keyToIndex[i]
     encryptedword += VTable[count][Vindex]
     if(count!=2):
         count+=1
     else:
         count = 0;
print(encryptedword)
