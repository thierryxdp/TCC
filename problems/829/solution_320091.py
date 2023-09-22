def soma_h(n):
    '''Função que retorna soma da lista de um numero n invertido'''
    '''int -> float'''
    s=0
    k = 1
    for numero in range(1, n+1):
        k = 1/numero
        s += k
	return round(s,2)