vC=0
cC=0
vow=["a","e","i","o","u"]
fd=open("letter.data","r")
vF=open("vowel.data","w")
cF=open("consonant.data","w")
for l in fd.read().split("\n"):
	arr=l.split("\t")
	if(arr[1] in vow and vC<2000):
		vF.write(l+" \n")
		vC+=1
	elif(cC<2000):
		cF.write(l+" \n")
		cC+=1
	if(vC==cC==2000):
		break
fd.close()
vF.close()
cF.close()