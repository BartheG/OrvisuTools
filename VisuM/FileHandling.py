from __impvisu__ import *

class FileHandling:
	def __init__(self,data):
		self.prefix_data,self.dir_data=data
		self.s_datapath=[]
		self.allfilesdata={}

	def getFilenames(self,pattern,dirdata):
		return utilsfunc.findMatch(
			pattern,
			dirdata
		)

	def getOneFile(self,):
		return self.allfilesdata[
			OpDict.moveIntoList(
				'Choose the file to plot',
				self.s_datapath
			)
		]

	def getMultipleFiles(self,):
		return [i for i in self.allfilesdata.values()]

	def run(self):
		self.datafilenames=self.getFilenames(self.prefix_data,self.dir_data)
		if len(self.datafilenames)<=0:
			raise FileNotFoundError
		self.s_datapath=utilsfunc.sortByName(self.datafilenames)
		for it,path in enumerate(self.s_datapath):
			print(it,' ',end=' ',flush=True)
			self.allfilesdata[path]=(convertLoadedData.protoToNumpy(path))