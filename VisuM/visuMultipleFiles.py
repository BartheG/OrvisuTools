import sys,os
import numpy as np
import matplotlib.pyplot as plt

from __impvisu__ import *
import commonFunc

class VisuMultipleFiles:
	def __init__(self,data):
		self.allfilesdata = data

	def getNeededValues(self):
		self.tkey=OpDict.moveIntoList('Choose time between the following values:',self.timekey)
		self.ekey=OpDict.moveIntoList('Choose element to plot:',self.varkey)
		self.log=commonFunc.handlePrintOfCustomParam(
			(
				'\n0\t->\tUse log10 on values',
				'\n1\t->\tDo not use log10 on values'
			),
			2
		)

	def getSavedInfosFromFiles(self):
		# for it,path in enumerate(self.filenames):
		# 	print(it,' ',end=' ',flush=True)
		# 	self.allfilesdata.append(convertLoadedData.protoToNumpy(path))
		# print('')
		self.timekey=[i for i in set().union(*(d.keys() for d in self.allfilesdata))]
		self.varkey=[i for i in set().union(*(d[i].keys() for d in self.allfilesdata for i in self.timekey if i in d.keys()))]

	def compute(self):
		av_data=[]
		know_id=[]
		for i in self.allfilesdata:
			n_data,know_id=OpDict.getNewShappedArray(3,i[self.tkey][self.ekey],know_id)
			av_data.append(
				np.average(
					np.ma.masked_where(
						n_data==0,
						n_data
					)
				)
			)
		return av_data if self.log else np.log10(av_data)

	def drawplot(self,x,y):
		plt.plot(x,y)
		plt.title(self.ekey)
		plt.show()

	def expData(self):
		self.getSavedInfosFromFiles()
		self.getNeededValues()
		return self.allfilesdata,self.tkey,self.ekey,self.log

	def run(self):
		x = [i for i,_ in enumerate(self.allfilesdata)]
		self.getSavedInfosFromFiles()
		self.getNeededValues()
		av_data = self.compute()
		self.drawplot(x,av_data)

def tempPlotMultipleFiles(func):
	data=func.getOnlyFilenames()
	if data==None:
		print('Error with data, you need to reload a dataset')
		return
	VisuMultipleFiles(data).run()

# ###LOCAL TEST###
# def main():
# 	v = VisuMultipleFiles('return_of_the_witch*.out','/Users/guillaume/Desktop/GuillaumeDevProd/WitchXCidre/ProjectRun/inputs/')
# 	v.run()

# if __name__ == '__main__':
# 	main()
# ###LOCAL TEST###
