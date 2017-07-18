#Python 3
import hashlib

#Open and read replay file
nFile = input("Replay: ")
hFile = open(nFile, 'rb')
cFile = hFile.read()
hFile.close()

#Find hash
hashLoc = 0x7
hashLen = cFile[hashLoc-1]
replayMapHash = cFile[hashLoc:hashLoc+hashLen]

#Open new map
nMap = input("Map to switch replay to: ")
hMap = open(nMap, 'rb')
cMap = hMap.read()
hMap.close()

#Make a hash for the new map
h = hashlib.md5()
h.update(cMap)
newMapHash = h.hexdigest()
print(newMapHash)

#Put new hash in
cFile = list(cFile)
cFile[hashLoc:hashLoc+hashLen] = list(bytes(newMapHash.encode("UTF-8")))
cFile = bytes(cFile)

#Generate new replay
nOutFile = "generated replay.osr"
hOutFile = open(nOutFile, "wb")
hOutFile.write(cFile)
hOutFile.close()
