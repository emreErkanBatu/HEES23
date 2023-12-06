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


st=time.time()
orgLen,compLen,compressedData,compRatio=encode.encodeData(message)
et=time.time()
processTime = round(et - st,3) 

print("\nOriginal Data",orgLen," Bits")
print("Compressed Data",compLen," Bits")

print("Compression Ratio: %",compRatio)

print("Process Time:",processTime)


fName=fName+"Decode"
with open(fName+'.txt', 'w') as f:
    f.writelines(compressedData)





