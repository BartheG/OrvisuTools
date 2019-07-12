import os
import numpy as np
import matplotlib.pyplot as plt

from __impvisu__ import *
import commonFunc

class ShowTemporalGraph:
	def compute(self):
		av_data=[]
		know_id=[]

		for i in self.x_cut:
			n_data,know_id=OpDict.getNewShappedArray(3,self.data[i][self.ekey],know_id)
			av_data.append(
				np.average(
					np.ma.masked_where(
						n_data==0,
						n_data
					)
				)
			)
		return (av_data,know_id) if self.log else (np.log10(av_data),know_id)

	def chooseCustomParam(self,):
		self.log=commonFunc.handlePrintOfCustomParam(
			(
				'\n0\t->\tUse log10 on values',
				'\n1\t->\tDo not use log10 on values'
			),
			2
		)

	#Plot the data depending on the time
	def timeplot(self,val,title,idxtab):
		plt.scatter(self.x_cut,val)
		plt.plot(self.x_cut,val)
		#plt.ylim(0,15)
		plt.title(title+' '+' '.join(str(idxtab)))
		plt.show()

	def chooseWhichParam(self,):
		self.ekey=OpDict.moveIntoDict('Choose element to plot:',self.data,subdict=True)
		self.x1=OpDict.moveIntoDict('Choose range of time to plot the data\nChoose time between the following values:',self.data)
		self.x2=OpDict.moveIntoDict('Choose time between the following values:',self.data)
		self.x_cut = [i for i in self.data.keys() if (float(self.x1)<=float(i)<=float(self.x2))]
		self.chooseCustomParam()

	def expData(self,data):
		self.data=data
		self.chooseWhichParam()
		return self.data,self.x_cut,self.ekey,self.log

	#Writting (time by plot)
	def run(self, data):
		self.data=data
		self.chooseWhichParam()
		val,idxtab=self.compute()
		self.timeplot(val,self.ekey,idxtab)

def tempPlotOneFile(func):
	data=func.getOnlyFile()
	if data==None:
		print('Error with data, you need to reload a dataset')
		return
	ShowTemporalGraph().run(data)


# def main():
# 	ShowTemporalGraph().run(sys.argv[1])

# if __name__ == '__main__':
# 	main()