from __impvisu__ import *

class FileHandling:
	def __init__(self,protodata,data):
		self.prefix_proto,self.dir_proto=protodata
		self.prefix_data,self.dir_data=data
		self.s_datapath=[]
		self.s_protopath=[]

		self.allfilesdata={}

	def getFilenames(self,pattern,dirdata):
		return utilsfunc.findMatch(
			pattern,
			dirdata
		)

	def wrapGetFilenames(self,):
		self.protofilenames=self.getFilenames(self.prefix_proto,self.dir_proto)
		self.datafilenames=self.getFilenames(self.prefix_data,self.dir_data)

	def getOneFile(self,):
		if len(self.s_datapath)!=0 and len(self.s_protopath)!=0:
			idx=OpDict.moveIntoList('Choose the file to plot',self.s_datapath)
			return self.allfilesdata[idx],self.s_protopath[self.s_datapath.index(idx)]
		return None,None

	def getMultipleFiles(self,):
		if len(self.s_datapath)!=0 and len(self.s_protopath)!=0:
			return [i for i in self.allfilesdata.values()],self.s_protopath
		return None

	def getOnlyFilenames(self,):
		if len(self.s_datapath)!=0:
			return [i for i in self.allfilesdata.values()]
		return None

	def getOnlyFile(self,):
		if len(self.s_datapath)!=0:
			idx=OpDict.moveIntoList('Choose the file to plot',self.s_datapath)
			return self.allfilesdata[idx]
		return None

	def run(self):
		self.wrapGetFilenames()
		print(len(self.datafilenames),len(self.protofilenames))
		if len(self.datafilenames)!=0:
			self.s_datapath=utilsfunc.sortByName(self.datafilenames)
		if len(self.protofilenames)!=0:
			self.s_protopath=utilsfunc.sortByName(self.protofilenames)
		if len(self.datafilenames)!=0:
			for it,path in enumerate(self.s_datapath):
				print(it,' ',end=' ',flush=True)
				self.allfilesdata[path]=(convertLoadedData.protoToNumpy(path))