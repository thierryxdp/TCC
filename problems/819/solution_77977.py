def filtraMultiplos(l,n):
    '''recebe uma lista de números(l) e um número(n), e retorna outra lista contendo todos os
    elementos da lista original que forem divisíveis por n; list, int -> list'''
	l1 = []
	contador = 0
	while contador < len(l):
    	if l[contador]%n == 0:
        	l1.append(l[contador])
    	contador = contador + 1
    return l1