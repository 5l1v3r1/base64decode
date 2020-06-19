from base64 import *

flagFile = open('encodedflag.txt', 'r').read()

decodedList = [flagFile]

for i in range(5):
    decoded = b16decode(decodedList[i])
    decodedList.append(decoded)

for x in range(5,10):
    decoded = b32decode(decodedList[x])
    decodedList.append(decoded)

for y in range(10,15):
    decoded = b64decode(decodedList[y])
    decodedList.append(decoded)

print(decodedList[15])
