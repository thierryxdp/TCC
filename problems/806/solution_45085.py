def colisao(tup,tup1):
	'''tuple, tuple --> bool'''
    return tup[2] > tup1[0] and tup1[2] > tup[0] and tup[3] > tup1[1] and tup1[3] > tup[1]