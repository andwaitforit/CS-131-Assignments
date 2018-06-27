# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:43:45 2018

@author: ahorgan
"""
"""
#Sum of Digits in a String

n = input("Enter a string of numbers")
sumDig = 0
for i in range(0,len(n)):
    nDig = eval(n[i])
    #print(nDig)
    sumDig += nDig
    
print(sumDig)
 
    
# Average Number of Words



file = open('text.txt', 'r')

content = file.readlines()
totalLines = 0
wordCount = 0
for i in content:
   #print(i)
   totalLines += 1
   words = i.split()
   #print(words)
   wordCount += len(words)
   #print(wordCount)
wordAvg = wordCount/totalLines
print("The average number of words per sentence is:", wordAvg)


#Word Separator
def main():
    sentence = input("Input a sentence to be split:")
    newString = sentence[0]
    for i in sentence[1:]:
       # print(i)
        if i.istitle() == True:
            newString += " " + i.lower()
            #print(i, "Is upper case")
        else:
            newString += i
    print(newString, end = ".")  
    
main()
"""

#PowerBall Lottery
def main():
    from pprint import pprint
    file = open('pbnumbers.txt', 'r')

    content = file.readlines()
    pbList = []
    pbNum = []
    pbNumCount = []
    for i in content:
        pbList.append(i[:-4].split(" "))
        pbNum.append(i[14:-1])
    print(pbNum)
    #print(pbList)
    for j in pbList:
        for k in j:
            for x in range(0,69):
                counter(j,x)
    for l in pbNum:
        for x in range(0,27):
            pbNumCount += counter(l,x)
            print(pbNumCount)
def counter(l1, x):
    count = 0
    for ele in l1:
        if (ele == x):
            count += 1

    return count










main()


    