def filtra_pares (t):
	'''Recebe tupla com quatro elementos inteiros e retorna
    apenas os pares da tupla original em ordem'''
    '''int => int'''
    
	tuple2 = tuple()
    
	if (t[0]%2)==0:
		tuple2 = tuple2 + (t[0],)
	
    elif (t[1]%2)==0:
		tuple2 = tuple2 + (t[1],)
	
    elif (t[2]%2)==0:
		tuple2 = tuple2 + (t[2],)
	
    elif (t[3]%2)==0:
		tuple2 = tuple2 + (t[3],)
        
	return tuple2