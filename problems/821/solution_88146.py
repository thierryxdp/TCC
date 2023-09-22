def fatorial(numero):
    '''Retorna o fatorial do numero dado
    int -> int'''
    k = numero
    listafatorial = []
    while k > 1:
        list.append(listafatorial,k)
        k = k - 1
	
    fatorial = 1
    indice = 0
    while indice < len(listafatorial):
        fatorial = fatorial*(listafatorial[indice])
        indice += 1
	return fatorial