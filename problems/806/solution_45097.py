def colisao(tup,tup1):
	'''tuple, tuple --> bool'''
    return tup[2] > tup1[0] or tup1[2] > tup[0] or tup[3] > tup1[1] or tup1[3] > tup[1]