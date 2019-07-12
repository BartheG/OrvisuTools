import sys,os

import writeVisuOutput
import commonFunc
from __impvisu__ import *

import visuMultipleFiles
import temporalSavedData

sys.path.append('../ProtocCommunication/PythonClient/')
import inputWitch
import DataProtoHandling

class VisuForAnimation:
	def __init__(self,data,proto):
		self.writevisuout = writeVisuOutput.WriteVisuOutput()
		self.protofilenames=proto
		self.data_data=data

	def compute(self):
		idx_c=[]
		it=0
		for data,proto in zip(self.all_witch_data,self.protofilenames):
			dph=DataProtoHandling.DataProtoHandlingFromCidre()
			file=open(proto,'rb')
			pt_data=b"".join(file.readlines())
			file.close()

			to_trans,idx_c=OpDict.getNewShappedArray(3,data[self.tkey][self.ekey],idx_c)
			dph.setCidreData(pt_data)
			dph.setAlt(to_trans.shape[0],to_trans.shape[1])
			dph.setAltR(to_trans.shape[0],to_trans.shape[1])
			to_write=dph.ajustThicknessByZ(
				to_trans,
				to_trans.shape[0],
				to_trans.shape[1],
				to_trans.shape[2],
				dph.getMapOfAltRego(
					to_trans.shape[0],
					to_trans.shape[1]
				),
				self.isLog
			)
			self.writevisuout.draw_magage(
				'./results/map_'+str(it)+'.out',
				to_write.shape[0],
				to_write.shape[1],
				to_write.shape[2]
			)
			self.writevisuout.run(
				to_write,
				'ubc',
				'./results/model_'+str(it)+'.out',
				bedrock=True
			)
			it+=1

	def run(self):
		self.all_witch_data,self.tkey,self.ekey,self.isLog=visuMultipleFiles.VisuMultipleFiles(
			self.data_data
		).expData()
		self.compute()

def anim(func):
	data,proto=func.getMultipleFiles()
	if data==None and proto==None:
		print('Error with data, you need to reload a dataset')
		print('Error with protobuf data, you need to reload protobuf files')
		return
	VisuForAnimation(data,proto).run()


def main():
	#glob='/Users/guillaume/Desktop/SaveVracWitchXCidre/WitchXCidre08_07_19_15*15/'
	glob=sys.argv[1]
	VisuForAnimation(
		('cidre_data_*.out',glob+'exp_data/'),
		('return_of_the_witch*.out',glob+'inputs/')
	).run()

if __name__ == "__main__":
	main()
