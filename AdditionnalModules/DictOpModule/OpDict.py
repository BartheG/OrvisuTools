def getRecursIndex(data,idx=False):
	if idx is not False and idx in range(len(data)):
		return list(data)[idx]
	try:
		input_t=input()
		idx=int(input_t)
	except KeyboardInterrupt:
		exit()
	except:
		pass
	return getRecursIndex(data,idx)

def moveIntoDict(msg,data,subdict=False):
	if type(data) != dict:
		raise TypeError
	if len(data.keys())==0:
		raise IndexError
	toCheck=data.keys() if subdict == False else [i for i in set().union(*(data.values()))]
	d_keys = ["{}\t->\t{}".format(key,idx) for key,idx in enumerate(toCheck)]
	print(msg+'\n'+'\n'.join(d_keys))
	return getRecursIndex(toCheck)

def moveIntoList(msg,data):
	d_keys = ["{}\t->\t{}".format(key,idx) for key,idx in enumerate(data)]
	print(msg+'\n'+'\n'.join(d_keys))
	return getRecursIndex(data)

def getNewShappedArray(shapewanted,data,old=[],idx_l=[]):
	dshape = data.shape
	if len(dshape) <= shapewanted:
		return data,idx_l
	print('Choose index between 0 and',dshape[0])
	idx=getRecursIndex(range(dshape[0])) if len(old)==0 else old.pop()
	idx_l.append(idx)
	return getNewShappedArray(shapewanted,data[idx],old=old,idx_l=idx_l)