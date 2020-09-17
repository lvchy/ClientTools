# -*- coding: utf-8 -*-

def encryptFile(file, newfile=None):
  f = open(file, 'rb')
  b = f.read()
  f.close()
  ba = bytearray(b)
  for i in range(len(ba)):
    ba[i] = (~ba[i]+1)&0xff
  newb = bytes(ba)
  if newfile == None:
    newfile = file
  f = open(newfile, 'wb')
  f.write(newb)
  f.close()
  
def decryptFile(file, newfile=None):
  f = open(file, 'rb')
  b = f.read()
  f.close()
  ba = bytearray(b)
  for i in range(len(ba)):
    ba[i] = (~(ba[i]-1))&0xff
  newb = bytes(ba)
  if newfile == None:
    newfile = file
  f = open(newfile, 'wb')
  f.write(newb)
  f.close()

if __name__ == "__main__":
  # encryptFile(r'D:\svn\Raid\Client\1.0\Assets\Lua\battle\manager.lua')
  # decryptFile(r'D:\svn\Raid\Client\1.0\Assets\Lua\battle\manager.lua.enc')
  pass