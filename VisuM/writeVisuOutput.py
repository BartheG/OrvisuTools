import numpy
import time

class WriteVisuOutput:
	def __init__(self):
		self.choice_read = {
			'ubc':self.writeUBC,
			'plotly':self.writePlotly
		}

	#Write .csv files depending on 3D array to use plotly visualization
	def writePlotly(self):
		if len(self.data.shape) != 3:
			return False
		numpy.savetxt(self.filename+'.map',self.data.shape,newline=" ")
		for i in range(self.data.shape[2]):
			numpy.savetxt(self.filename+str(i)+".csv", (self.data[:,:,i]), delimiter=",")
		return True

	#Write ubc type file to use PVGeo visualization
	def writeUBC(self):
		if len(self.data.shape) != 3:
			return False
		n_data = numpy.flip(self.data.ravel())
		with open(self.filename, mode='wt', encoding='utf-8') as myfile:
			if self.bedrock:
				myfile.write('\n'.join(str(line).replace('-100.0','oui') for line in n_data))
			else:
				myfile.write('\n'.join(str(line).replace('-100.0','oui').replace('100.0','oui') for line in n_data))
		return True

	#Determine which write option use
	def run(self,toWrite,outFormat,filename,bedrock=False):
		if outFormat in self.choice_read.keys():
			self.data = toWrite
			self.filename = filename
			self.bedrock = bedrock
			print('Write complete...') if self.choice_read[outFormat]() else print('Error on data')
		else:
			print('Write format not recognized...')

	#Draw mapage from witch simulation to define the domain to display
	def draw_magage(self,filename,x,y,z):
		file = open(filename,'w')
		file.write(str(x)+' '+str(y)+' '+str(z)+'\n')
		file.write('1 1 1\n')
		xlist = ' '.join('{}'.format('1') for k in range(x))
		ylist = ' '.join('{}'.format('1') for k in range(y))
		zlist = ' '.join('{}'.format('1') for k in range(z))
		file.write(xlist+'\n'+ylist+'\n'+zlist)
		file.close()
		print('Write of mapage...')

def main():
	data = numpy.linspace(1,80,60*60*60)
	data = data.reshape((
		60,60,60
	))

	w = WriteVisuOutput()
	start = time.time()
	#w.run(data,'ubc','./test.file.out')
	print(time.time() - start)

if __name__ == '__main__':
	main()