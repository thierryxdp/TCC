def filtraMultiplos(l,n):
    '''Retorna uma lista com os múltiplos de n, a partir
    de uma lista de numeros e o valor n em si; list, float
    -> list'''
    i = 0
    ln = []
    while i<len(l):
        if l[i]%n==0:
        	list.append(ln, l[i])
    	i += 1
    return ln