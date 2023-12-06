# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:00:00 2023
@author: Emre ERKAN
"""
import codeConvert 
import time




encode=codeConvert.codeDecode() 

fName="text4"
with open(fName+'.txt') as f:
    message = f.read()

# message=message[:50000]
# message="test sentence"
# message="hello world"
    
# # message="Adi: Emre\nSoyadi:ERKAN\nKurumu:Batman Universitesi\nAdi: Emre\nSoyadi:ERKAN\nKurumu:Batman Universitesi\nAdi: Emre\nSoyadi:ERKAN\nKurumu:Batman Universitesi\nAdi: Emre\nSoyadi:ERKAN\nKurumu:Batman Universitesi\nAdi: Emre\nSoyadi:ERKAN\nKurumu:Batman Universitesi\n"
# message="hello world"
# message=message*1000
st=time.time()
orgLen,compLen,compressedData,compRatio=encode.encodeData(message)
et=time.time()
processTime = round(et - st,3) 
# print("\n-----------------Original Data-----------------")
# print(message,'\n')

# print("-----------------Compressed Data-----------------")
# print(compressedData)

print("\nOriginal Data",orgLen," Bits")
print("Compressed Data",compLen," Bits")

print("Compression Ratio: %",compRatio)

print("Process Time:",processTime)


fName=fName+"Decode"
with open(fName+'.txt', 'w') as f:
    f.writelines(compressedData)





