# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:42:28 2017

@author: rajar
"""


keysfile = open("hotelF-train.txt", "r")
predictedfile = open("traindataoutput7.txt", "r")

totalkeys = 0.0
correctpred = 0.0
accuracy = 0.0
pred = ""
for i in predictedfile:
    totalkeys += 1
    pred = i[8:].strip()
    #print(i[8:])
    if (pred == "T"):
        #print("Reached here!")
        correctpred += 1
accuracy = correctpred/totalkeys
print(correctpred, totalkeys, accuracy)