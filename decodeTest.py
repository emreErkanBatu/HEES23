# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:00:00 2023
@author: Emre ERKAN
"""
import codeConvert  
import time
decode=codeConvert.codeDecode() 

fName="text4Decode"
with open(fName+'.txt') as f:
    compressedData = f.read()

# compressedData=
st=time.time()
text=decode.decodeData(compressedData)
et=time.time()
processTime = round(et - st,3) 
# print(text)
