# -*- coding: utf-8 -*-

import json
import collections
from collections import Counter 

with open('convertTable.json') as f:
  veri = json.load(f)

class codeDecode: 
    
    def specialDecToBase(self,number,base,ch):
        dividend=number
        divisor=base
        count=0
        newBase=''
        status=0
        while(dividend>=divisor):
            remainder=dividend%divisor
            dividend=int(dividend/divisor)
            newBase=str(remainder)+newBase
            count=count+1
            status=1
        if(status==1):
            newBase=count*ch+str(dividend)+newBase
        else:
            newBase=str(dividend)  
        return newBase

    def encBitDec(self,data):
        cnvrt={'0': '0', '1': '10', '2': '1111', '3': '1101', '-': '1100', '4': '11100', '5': '111011', '6': '111010'}
        # print (data)
        # print ()
        newData1=''
        kod=''
        x=0
        count=0
        fristChar=data[0]    
        while(x<len(data)):
            while(x+1<len(data) and data[x]==data[x+1] ) :
                count=count+1
                x=x+1
            # newData1=newData1+specialDecToOct(count)
            newData1=newData1+self.specialDecToBase(count,7,'-')
            count=0
            x=x+1 
        # print(newData1)
        for i in range(len(newData1)):
            kod=kod+cnvrt[newData1[i]]   
        kod=fristChar+kod
        # print("kodlanan data",newData1)
        # print()
        # print(kod)
        return kod
    
    def decBitDec(self,data):
        cnvrt={'0': '0', '1': '10', '2': '1111', '3': '1101', '-': '1100', '4': '11100', '5': '111011', '6': '111010'}
        fristChar=data[0] 
        if fristChar=='0':
            secondChar='1'
        else:
            secondChar='0'
        data=data[1:]
        keylist=list(cnvrt.keys())
        newData1=''
        x=0
        while(x<len(data)):
            for i in range(0,8):
                chs=cnvrt[keylist[i]]
                l=len(chs)
                if (data[x:x+l]==cnvrt[keylist[i]]):
                    newData1=newData1+keylist[i]
                    x=x+l
                    break    
        numberList=[]
        datalist=[]
        x=0
        count=0
        # newData1='-10'
        while(x<len(newData1)):
            while(newData1[x]=='-'):
                count=count+1
                x=x+1
            octalNum=newData1[x:x+count+1]
            carpan=int(octalNum,7) 
            # print("çarpan:",carpan)
            numberList.append(carpan)
            if (len(numberList)%2==1):
                datalist.append(fristChar)
            else:
                datalist.append(secondChar)           
            x=x+count+1
            count=0
            # if (x>=len(newData1)):
            #     break
                
        # print(numberList)
        # print(datalist)   
        # print("cevap",octalNum)       
        # print(newData1)
        binaryCode=''
        for i in range(0,len(numberList)):
            binaryCode=binaryCode+(numberList[i]+1)*datalist[i]
        # print(binaryCode)
        return binaryCode
    
    def compStage0(self,data,mostCh):
        newData=''
        x=0    
        while(x<len(data)):
            currentCh=data[x]
            y=0
            d=0
            while(currentCh==data[x:x+1]):
                y=y+1
                x=x+1
                d=1
            if(d==0):
                x=x+1
                d=0
            if(y!=0):
                y=y-1
            newData=newData+y*mostCh+currentCh              
        return newData
    
    def compStage0Dec(self,data,index):
        newData=''
        x=0 
        y=0
        while(x<len(index)):
            if index[x]=='0':
                newData=newData+'|'
                x=x+1
            else:
                newData=newData+data[y]
                x=x+1
                y=y+1            
                # if (y>=len(data)):
                #     break
        return newData

    def compStage0a(self,data):
        newData=''
        x=0    
        while(x<len(data)):
            currentCh=data[x]
            if(currentCh=='|'):
                newData=newData+'0'
            else:
                newData=newData+'1'            
            x=x+1              
        return newData 

    def chrIndex(self,data,ch):
        cnt=0
        mainData=''
        indexData=self.compStage0a(data)
        for i in range(0,len(data)):
            if (data[i]!=ch):
                cnt=0
                mainData=mainData+data[i]
            elif (data[i]==ch):
                cnt=cnt+1
        return mainData,indexData 
    
    def chrIndexDec(self,data,ch):
        newData=''
        x=0
        count=0
        d=0
        while(x<len(data)):
            while(data[x]==ch):
                count=count+1
                x=x+1
                d=1
            if(d==1):
                newData=newData+count*data[x]
                d=0
                count=0
            else:
                newData=newData+data[x]
                x=x+1
        return newData
    
    def change(self,data,ch1,ch2):
        newData=''
        if(ch1=='|' and ch2=='|'):
            newData=data
        else:
            for i in range(0,len(data)):
                if (data[i]==ch1):            
                    newData=newData+ch2
                if (data[i]==ch2):
                    newData=newData+ch1
                if (data[i]!=ch2 and data[i]!=ch1):
                    newData=newData+data[i]
        return newData
    
    def mostCommon(self,data):
        charNumList=collections.Counter(data).most_common()
        chCount=len(charNumList)
        mostCh=collections.Counter(data).most_common(chCount)[0][0]    
        if (mostCh!='|'):
            changeCh='|'+mostCh
        else:
            changeCh='||'
        return changeCh
    
    def changeChBits(self,ch):
        if(ch=='|'):
            bits='1000'
        else:
            bits=bin(int(ch))[2:]
        bits=(4-len(bits))*'0'+bits
        return bits
    
    def symbolToBit(self,data):
        chTable={'|':'1','0':'0111','1':'0110','2':'0101','3':'0100','4':'0011','5':'0010','6':'0001','7':'0000'}
        x=0 
        newData=''
        limit=len(data)
        while(x<limit):
            newData=newData+chTable[data[x]]
            x=x+1
        return newData
    
    def binToSym(self,data):
        newData=''
        x=0
        while(x<len(data)):
            sym=int(data[x:x+3],2)
            newData=newData+str(sym)
            x=x+3
        return newData
    
    def octToBin(self,data):
        newData=''
        x=0    
        while(x<len(data)):
            bits=bin(int(data[x]))[2:]
            bits=(3-len(bits))*'0'+bits
            newData=newData+bits
            x=x+1    
        return newData
    
    def sembolOctal(self,number):
        number=str(oct(number))
        octLen=len(number)
        number=number[2:octLen]
        length=len(number)-1
        sonuc=length*'|'+number
        return sonuc

    def assembleIndex(self,index1,index2):
        size=bin(len(index2))
        size=size[2:len(size)]
        size=(22-len(size))*'0'+size
        data=size+index1+index2
        return data
    
    def partitionIndex(self,index):
        part=int(index[0:22],2)
        getPart=len(index)-part
        index1=index[22:getPart]
        index2=index[getPart:len(index)]    
        return index1,index2
    
    def dataStageLen(self,dataStage):
        size=bin(len(dataStage))
        size=size[2:len(size)]
        size=(22-len(size))*'0'+size
        return size

    def addBW(self,data,BW):
        data=self.sembolOctal(BW)+data
        return data
    
    def findBW(self,data):
        x=0
        limit=len(data)
        while(x<limit and data[x]=='|'):
            x=x+1
        BW=int(data[x:2*x+1],8)
        data=data[2*x+1:]        
        return data,BW  
    
    def specialCh(self,data):
        specialChIndex=0
        for i in range(0,len(data)):
            if(data[i]=='$'):
                specialChIndex=i
                data=data.replace('$', '') 
                break
        return data,specialChIndex
    
    def encodeBW(self,data,speCh):
        data=data+speCh
        m = sorted(data[-i:] + data[:-i] for i in range(len(data)))
        newData="".join(m[i][len(data)-1] for i in range(len(data)))
        # print(newData)
        newData=self.specialCh(newData)
        return newData
    
    def decodeBW(self,data,indx,ch):    
        c = Counter()
        c.update(data)  # text is a str, count chars
        # c
        charList=[key for key, _ in c.most_common()]
        charList.append(ch)
        charList=sorted(charList)
     
        listData=[]
        sortedList=[]
        newData=''
        data=data[:indx]+'$'+data[indx:]
    
        for i in range(0,len(data)):
            listData.append((data[i],i))
        # sortedList.append((ch,startPOS))
        for i in range(0,len(charList)):
            for j in range(0,len(listData)):
                if (listData[j][0]==charList[i]):
                    sortedList.append(listData[j])
          
        say=len(sortedList) 
        index=sortedList[0][1] 
    
        for i in range(0,say-1):
            newData=newData+sortedList[index][0]
            index=sortedList[index][1]
        
        return newData
    

    
    def encText(self,original_text):
        encodeText=""
        topveri=""
        cNum=len(original_text)
        for i in range(0,cNum):
            for j in range(0,97):
                if veri["table"][j]["Dec"]==ord(original_text[i]):                     
                    encodeText=encodeText+veri["table"][j]["Bin"]
                    topveri=topveri+veri["table"][j]["symbolCode"]
                    break
        return encodeText,topveri

    def decText(self,comp_text):
        freqTable=['1','0111','0110','0101','0100','0011','0010','0001','0000']
        comp_text2=""
        decodeText=""
        while (0 != len(comp_text)):
            slenght=len(comp_text)
            for j in range(0,9):                
                hCode=freqTable[j]
                snr=len(hCode)
                if comp_text[0:snr]==hCode:
                    if j==0 :
                        comp_text2=comp_text2+'|'
                    else:
                        comp_text2=comp_text2+str(j-1)
                    comp_text=comp_text[snr:slenght]
                    break
            
        while (0 != len(comp_text2)):
            
            slenght=len(comp_text2)
            for j in range(0,97):
                hCode=comp_text2[0]
                for k in range(1,slenght):
                    if ord(comp_text2[k])==124:
                        hCode=hCode+'|'
                    else:
                        break
                snr=len(hCode)             
                if veri["table"][j]["symbolCode"]==hCode:                    
                    decodeText=decodeText+veri["table"][j]["Char"]
                    comp_text2=comp_text2[snr:slenght]
                    break                                
        return decodeText
    
    def encodeData(self,data):
        orgLen=8*len(data)
        symbolsBit,symbols=self.encText(data)
        # print(symbols)
    
        symbolsBW,BW0=self.encodeBW(symbols,'$') 
        # print(symbolsBW)
        
        symbolsBW=self.addBW(symbolsBW,BW0)
        # print(symbolsBW)
        
        changeChr1=self.mostCommon(symbolsBW)
        changeChrBits=self.changeChBits(changeChr1[1])
        
        symbolsBW=self.change(symbolsBW,changeChr1[0],changeChr1[1])
        # print(symbolsBW)
        
        dataStage1,indexStage1=self.chrIndex(symbolsBW,'|')
        
        dataStage2=self.compStage0(dataStage1,'|')
        
        
        # dataStage2,BW1=self.encodeBW(dataStage2,'$') #yeni ekledim
        # dataStage2=self.addBW(dataStage2,BW1)#yeni ekledim
        
        dataStage3,indexStage2=self.chrIndex(dataStage2,'|')
        
        # print(indexStage1)
        # print(indexStage2)
        # print(dataStage3)
        
        indexes=self.assembleIndex(indexStage1,indexStage2)
        # print(indexes)
        compressedIndexes=self.encBitDec(indexes)
        # print(compressedIndexes)
        
        if(len(indexes)>len(compressedIndexes)):
            compIndexes='1'
            useIndexes=compressedIndexes
        else:
            compIndexes='0'
            useIndexes=indexes
        
        dataStage3Bin=self.octToBin(dataStage3)
        dataStage3Len=self.dataStageLen(dataStage3Bin)
        
        compressedData=dataStage3Len+changeChrBits+compIndexes+dataStage3Bin+useIndexes
        # print(compressedData)
        compLen=len(compressedData)
        compRatio=round((1-(compLen/orgLen))*100,2)
        return orgLen,compLen,compressedData,compRatio
    
    def decodeData(self,compressedData):
        dataStage3Len=int(compressedData[:22],2)
        changeChrBits=int(compressedData[22:26],2)
        compIndexes=compressedData[26]
        dataStage3=self.binToSym(compressedData[27:27+dataStage3Len])
        useIndexes=compressedData[27+dataStage3Len:]
        
        if compIndexes=='1':
            indexes=self.decBitDec(useIndexes)
        else:
            indexes=useIndexes
        
        indexStage1,indexStage2=self.partitionIndex(indexes)
        
        dataStage2=self.compStage0Dec(dataStage3,indexStage2)
        
        dataStage1=self.chrIndexDec(dataStage2,'|')
        
        symbolsBW=self.compStage0Dec(dataStage1,indexStage1)
        
        if changeChrBits==8:
            changeChr1='||'
        else:
            changeChr1='|'+str(changeChrBits)
            symbolsBW=self.change(symbolsBW,changeChr1[0],changeChr1[1])
          
        symbolDataBW,BW0=self.findBW(symbolsBW)
        
        symbolData=self.decodeBW(symbolDataBW,BW0,'$')
        
        symbolsBit=self.symbolToBit(symbolData)
        text=self.decText(symbolsBit) 
        return text
    
class convert:
    def bin2hex(self,bin_text):
        hexTable=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        hexText=""
        textLenght=len(bin_text)
        bin_text=bin_text+(textLenght%4)*'0'
        hexLenght=int(len(bin_text)/4)
        
        for i in range(0,hexLenght):
            hexNum=0
            hexNum=int(bin_text[i*4])*8+int(bin_text[i*4+1])*4+int(bin_text[i*4+2])*2+int(bin_text[i*4+3])*1
            hexText=hexText+hexTable[hexNum]
                   
        return hexText
    
    def oneZeros(self,bin_text):
        zeros=0
        ones=0
        textLenght=len(bin_text)        
        for i in range(0,textLenght):
            if bin_text[i]=='0':
                zeros=zeros+1
            else:
                ones=ones+1                   
        return zeros,ones