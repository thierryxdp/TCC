def faltante(l:list)->int:
    '''retorna qual numero esta faltando na lista'''
    
    i=0
    
    while i < len(l):
        if l[i] -1 not in l and l[i] -1 != 0:
            return l[i] -1
        
		i += 1
	return l[-1] +1