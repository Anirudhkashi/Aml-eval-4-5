import neurolab as nl
import numpy
import copy
from hmm import *

XTr= []
YTr= []
XTe= []
YTe= []
letter= [float(0) for i in range(26)]
inp= [[0.0, 1.0]]* 129
net= nl.net.newff(inp, [20, 26], transf= [nl.trans.TanSig(),nl.trans.SoftMax()])

def getData():

	global XTr
	global YTr
	global YTe
	global XTe
	global vTr
	global cTr
	vTr=[]
	cTr=[]

	fp= open("vowel.data", "r")
	for line in fp.read().split("\n"):
		line= line.split('\t')
		XTr.append(line[6:-1])
		YTr.append(line[1])
	vTr=XTr[:1000]
	vTr= ["".join(i) for i in vTr]
	XTr=XTr[1000:]

	fp.close()

	fp= open("consonant.data", "r")
	for line in fp.read().split("\n"):
		line= line.split('\t')
		XTr.append(line[6:-1])
		YTr.append(line[1])
	cTr=XTr[1000:2000]
	cTr= ["".join(i) for i in cTr]
	XTr=XTr[:1000]+XTr[2000:]

	fp.close()

	# for i in range(len(XTr)):
	# 	XTr[i]= [int(j) for j in XTr[i]]
	XTr= ["".join(i) for i in XTr]
	addBit()

	for i in range(len(XTr)):
		XTr[i]= [float(j) for j in XTr[i]]

	discretize()	

	XTe= meldLists(XTr[800:1000],XTr[1800:])
	YTe= meldLists(YTr[800:1000],YTr[1800:])
	XTr= meldLists(XTr[:800],XTr[1000:1800])
	YTr= meldLists(YTr[:800],YTr[1000:1800])



	train()
	test()

def addBit():
	global XTr
	global vTr
	global cTr
	hmm=HMM(vTr,cTr)

	bitList= hmm.yVals(XTr)

	for i in range(len(bitList)):
		XTr[i]+= str(bitList[i])

def meldLists(lA,lB):
	tmp=[]
	for i in range(len(lA)):
		tmp.append(lA[i])
		tmp.append(lB[i])
	return tmp

def discretize():
	global YTr
	
	for i in range(len(YTr)):
		temp= copy.deepcopy(letter)
		YTr[i]= ord(YTr[i])-97.0
		temp[int(YTr[i])]= 1.0
		YTr[i]= temp


def train():
	global net	
	err = net.train(XTr, YTr, epochs= 20, show=1)

def test():

	global net
	ret= list(net.sim(XTe))

	count= 0
	totalCount= len(ret)


	for i in range(len(ret)):
		flag=1
		ret[i]= list(maxed(ret[i]))
		for j in range(len(ret[i])):
			if(ret[i][j]!= YTe[i][j]):
				flag=0
				break
		if(flag):
			count=count+1

	accuracy= (float(count)/float(totalCount))*100.0
	print str(accuracy)+ "%"


def maxed(lst):
	maxVal= lst[0]
	maxIndex= 0
	for i in range(len(lst)):
		if(lst[i]> maxVal):
			maxIndex= i
			maxVal= lst[i]

	for i in range(len(lst)):
		if(i== maxIndex):
			lst[i]= 1.0
		else:
			lst[i]= 0.0

	return lst

getData()