def filtra_pares (t):
	'''Recebe tupla com quatro elementos inteiros e retorna
    apenas os pares da tupla original em ordem'''
    '''int => int'''
    
	tuple2 = tuple()
    
	if (t[0]%2)==0:
		tuple2 = tuple2 + (t[0],)
	
    if (t[1]%2)==0:
		tuple2 = tuple2 + (t[1],)
	
    if (t[2]%2)==0:
		tuple2 = tuple2 + (t[2],)
	
    if (t[3]%2)==0:
		tuple2 = tuple2 + (t[3],)
        
	return tuple2