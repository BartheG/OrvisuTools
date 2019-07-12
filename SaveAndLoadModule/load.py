import struct_pb2

class StructLoad:
	def __init__(self):
		self.struct=struct_pb2.Data()

	def loadFile(self,filename):
		try:
			file=open(filename,'rb')
			self.struct.ParseFromString(file.read())
			file.close()
		except:
			pass

	def run(self,filename):
		self.loadFile(filename)
		return self.struct.data

def structLoad(filename):
	return StructLoad().run(filename)