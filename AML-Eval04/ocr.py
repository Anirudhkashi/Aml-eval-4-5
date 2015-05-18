import neurolab as nl
import numpy
import copy


XTr= []
YTr= []
XTe= []
YTe= []
letter= [float(0) for i in range(26)]
inp= [[0.0, 1.0]]* 128
net= nl.net.newff(inp, [16, 26], transf= [nl.trans.TanSig(), nl.trans.SoftMax()])

def getData():

	global XTr
	global YTr
	global YTe
	global XTe

	fp= open("letter.data", "r")
	for line in fp.read().split("\n")[:1000]:
		line= line.split('\t')
		XTr.append(line[6:-1])
		YTr.append(line[1])

	fp.close()

	discretize()

	for i in range(len(XTr)):
		XTr[i]= [float(j) for j in XTr[i]]

	XTe= XTr[800:]
	YTe= YTr[800:]
	XTr= XTr[:800]
	YTr= YTr[:800]

	train()
	test()

def discretize():
	global YTr
	
	for i in range(len(YTr)):
		temp= copy.deepcopy(letter)
		YTr[i]= ord(YTr[i])-97.0
		temp[int(YTr[i])]= 1.0
		YTr[i]= temp


def train():
	global net	
	err = net.train(XTr, YTr, show=1)

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