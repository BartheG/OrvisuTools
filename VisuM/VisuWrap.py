from __impwrap__ import *
from __impvisu__ import *
import commonFunc
import FileHandling

def getRecursInputStr(todisp='',data='',valid=False):
	if valid and len(data)!=0:
		return data
	try:
		data=input(todisp+'\n')
		print('Validate?')
		valid=commonFunc.handlePrintOfCustomParam(('0\t->\tNo','1\t->\tYes'),2)
	except KeyboardInterrupt:
		exit()
	return getRecursInputStr(todisp,data,valid)

class VisuWrap:
	def __init__(self,startdir):
		self.allvisu={
			'Animation':visuForAnimation.anim,
			'3D Plot':visuSavedData.plotOneFile,
			'Evolution au cours du temps':temporalSavedData.tempPlotOneFile,
			'Evolution sur plusieurs fichiers':visuMultipleFiles.tempPlotMultipleFiles,
			'Change paths':self.setPath,
		}
		self.startdir=startdir

	def sendToVisu(self,):
		self.allvisu[self.torun](
			self.fread
		)

	def setPath(self,_=None):
		self.pathfiles=self.startdir+'/'+getRecursInputStr(
			'Path to saved files (concatenation to '+self.startdir+') :'
		)
		self.prefixfiles=getRecursInputStr(
			'Pattern of saved files (ex: return_of_the*.out):'
		)
		self.pathproto=self.startdir+'/'+getRecursInputStr(
			'Path to protobuf files (concatenation to '+self.startdir+'):'
		)
		self.prefixproto=getRecursInputStr(
			'Pattern of protobuf files (ex: datap*.out):'
		)

	def run(self):
		self.setPath()

		self.fread=FileHandling.FileHandling(
			(self.prefixproto,self.pathproto,),
			(self.prefixfiles,self.pathfiles)
		)
		#Debug
		# self.fread=FileHandling.FileHandling(
		# 	('cidre_data*.out','../ProjectRun/exp_data/'),
		# 	('return_of_th*.out','../ProjectRun/inputs/')
		# )
		self.fread.run()
		while True:
			self.torun=OpDict.moveIntoDict('Choose type of visualization/command',self.allvisu)
			try:
				self.sendToVisu()
			except:
				print('Avoid the crash')

def main():
	startdir='../ProjectRun/'

	VisuWrap(startdir).run()

if __name__ == "__main__":
	main()