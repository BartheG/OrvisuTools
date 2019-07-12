import numpy as np
import load

class ProtoToNumpy:
	def __init__(self,filename):
		self.data=load.structLoad(filename)

	def run(self):
		if len(self.data)==0:
			return False
		fdata={}
		for i in self.data:
			if i.key not in fdata:
				fdata[i.key]={}
			fdata[i.key][i.value.name]=np.array(
				np.frombuffer(
					i.value.data
				)
			).reshape(
				eval(
					i.value.shape
				)
			)
		return fdata

def protoToNumpy(filename):
	return ProtoToNumpy(filename).run()