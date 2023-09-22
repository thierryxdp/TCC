def colisao(tup,tup1):
	'''tuple, tuple --> bool'''
	if tup[2] < tup1[0]:
        return 'False'
    elif tup1[2] < tup[0]:
        return 'False'
    elif tup[3] < tup1[1]:
        return 'False'
    elif tup1[3] < tup[1]:
        return 'False'
    else:
        return 'True'