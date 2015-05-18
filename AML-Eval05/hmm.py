from myhmm_log import *

class HMM():
	def genModel(self,obslist):
		mod= MyHmmLog('debate_initial.json')
		mod.forward_backward_multi(obslist)
		return mod


	def yVals(self,vecVec):
		yVec=[]
		for i in vecVec:
			yVec.append(self.argMax(i))
		return yVec

	def argMax(self,vec):
		clss=1
		if(self.consonant_model.forward(vec)> self.vowel_model.forward(vec)):
			clss=0
		return clss


	def __init__(self,vTr,cTr):
		
		self.vowel_model= self.genModel(vTr)

		self.consonant_model= self.genModel(cTr)