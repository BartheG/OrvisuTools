import sys,os
import numpy as np
sys.path.append('../ProtocCommunication/PythonClient')
import writeVisuOutput

from __impvisu__ import *
import commonFunc
import DataProtoHandling
import inputWitch

class WriteSavedData:
	def __init__(self,protofile):
		self.writevisuout = writeVisuOutput.WriteVisuOutput()

		InputData = inputWitch.InputWitch('../ProjectRun/input_witch.txt',['anorthite','Albite','K-feldspar','Quartz','kaolinite','halloysite','Ca-smectite','Gibbsite'],8)
		init_data = InputData.run()

		#Initialize DataProtoHandling with protofile passed trought parameter
		self.dph = DataProtoHandling.DataProtoHandlingFromCidre()
		file = open(protofile, 'rb')
		data = b"".join(file.readlines())
		self.dph.setCidreData(data)
		self.dph.setAlt(init_data['x'],init_data['y'])
		self.dph.setAltR(init_data['x'],init_data['y'])


	#Wrap to read and minipulate saved witch files
	def run(self, data):
		self.fulldata = data
		self.chooseWhichPrint()
		self.convertToRealDomain()
		self.drawFiles()

	def chooseCustomParam(self,):
		self.log=commonFunc.handlePrintOfCustomParam(
			(
				'\n0\t->\tUse log10 on values',
				'\n1\t->\tDo not use log10 on values'
			),
			2
		)
		self.bedrock=commonFunc.handlePrintOfCustomParam(
			(
				'\n0\t->\tNo Bedrock',
				'\n1\t->\tBedrock'
			),
			2
		)

	#Choose writing options
	def chooseWhichPrint(self):
		#Read data from file
		data=self.fulldata
		if data==False:
			exit()
		#Simulation time
		self.timekey=OpDict.moveIntoDict('Choose time between the following values:',data)
		#Array to print
		self.ekey=OpDict.moveIntoDict('Choose element to plot:',data[self.timekey])
		#Get 3D array
		dshape = data[self.timekey][self.ekey].shape
		if len(dshape) < 3:
			return
		self.to_print,_=OpDict.getNewShappedArray(3,data[self.timekey][self.ekey])
		self.chooseCustomParam()

	#Transforms regolith thickness domain by adding real height of bedrock
	def convertToRealDomain(self):
		self.modtab = self.dph.ajustThicknessByZ(
			self.to_print,
			self.to_print.shape[0],
			self.to_print.shape[1],
			self.to_print.shape[2],
			self.dph.getMapOfAltRego(
				self.to_print.shape[0],
				self.to_print.shape[1])
			,self.log)

	#Executes write of data's
	def drawFiles(self):
		self.writevisuout.draw_magage(
			'./results/map_test_min_'
			+self.ekey
			+'_'
			+self.timekey
			+'.out',
			self.modtab.shape[0]
			,self.modtab.shape[1]
			,self.modtab.shape[2])
		self.writevisuout.run(self.modtab,'ubc','./results/test_min_'+self.ekey+'_'+self.timekey+'.out',bedrock=self.bedrock)

def plotOneFile(func):
	data,proto=func.getOneFile()
	if data==None and proto==None:
		print('Error with data, you need to reload a dataset')
		print('Error with protobuf data, you need to reload protobuf files')
		return
	WriteSavedData(proto).run(data)

def main():
	data=convertLoadedData.protoToNumpy('../ProjectRun/inputs/return_of_the_witch1562861906.929737.out')
	WriteSavedData('../ProjectRun/exp_data/cidre_data_400.00.out').run(data)

if __name__ == '__main__':
	main()