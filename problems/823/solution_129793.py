def faltante(L):
    '''Retorna o número que está flatando na lista L, de acordo com a ordem dada (1 a N);
    list -> int'''
    i = 0
    list.sort(L)
    while i< len(L):
        if L[i] != i+1:
            return i+1
        
        i = i+1
        
        
    else:
    	return L[len(L)-1] + 1