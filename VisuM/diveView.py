import numpy as np
import matplotlib.pyplot as plt
from __impvisu__ import *
import commonFunc

class DiveView:
	def __init__(self,filename):
		self.filename=filename

	def getFile(self):
		self.data=convertLoadedData.protoToNumpy(self.filename)
		if self.data==False:
			exit()

	def getParam(self,):
		self.timekey=OpDict.moveIntoDict('Choose time between the following values:',self.data)
		self.ekey=OpDict.moveIntoDict('Choose element to plot:',self.data[self.timekey])
		dshape = self.data[self.timekey][self.ekey].shape
		if len(dshape) < 3:
			return
		self.to_print,_=OpDict.getNewShappedArray(3,self.data[self.timekey][self.ekey])
		self.log=commonFunc.handlePrintOfCustomParam(
			(
				'\n0\t->\tUse log10 on values',
				'\n1\t->\tDo not use log10 on values'
			),
			2
		)

	def getValues(self,):
		self.to_disp=np.zeros((self.to_print.shape[0],self.to_print.shape[1]))

		for i in range(self.to_print.shape[0]):
			for j in range(self.to_print.shape[1]):
				idx_top=np.nonzero(self.to_print[i,j,:])[0][-1]
				self.to_disp[i,j]=self.to_print[i,j,idx_top] if self.log else np.log10(self.to_print[i,j,idx_top])

	def compute(self,):
		plt.imshow(self.to_disp)
		plt.colorbar()
		plt.show()

	def run(self,):
		self.getFile()
		self.getParam()
		self.getValues()
		self.compute()

def main():
	import sys
	if len(sys.argv)!=2:
		return
	DiveView(sys.argv[1]).run()

if __name__ == "__main__":
	main()