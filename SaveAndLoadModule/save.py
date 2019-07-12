import numpy as np
from datetime import datetime

import struct_pb2

class StructSave:
	def __init__(self):
		self.struct = struct_pb2.Data()

	def clearOrReadFile(self,filename,isErase):
		if isErase==True:
			open(filename,'w').close()
		else:
			try:
				file=open(filename,'rb')
				self.struct.ParseFromString(file.read())
				file.close()
			except FileNotFoundError:
				pass

	def fillStruct(self,name,data,shape,m_id):
		fill_data=self.struct.data.add()
		fill_data.key=m_id
		n_data=fill_data.value
		n_data.name=name
		n_data.data=data
		n_data.shape=shape

	def runIntoData(self,m_id,**kwargs):
		for key,data in kwargs.items():
			if type(data)!=np.ndarray:
				continue
			self.fillStruct(
				name=key,
				data=np.ndarray.tobytes(data),
				shape=str(data.shape),
				m_id=str(m_id),
			)

	def run(self,**kwargs):
		custom_id=kwargs.get('id','m_id')
		filename=kwargs.get('filename','structdata.out')
		self.clearOrReadFile(filename,kwargs.get('clear_file',False))
		self.runIntoData(custom_id,**kwargs)
		try:
			file=open(filename,'wb')
			file.write(self.struct.SerializeToString())
			file.close()
			print('Write complete:',filename)
		except:
			print('Error: on write')

def structSave(**kwargs):
	StructSave().run(**kwargs)