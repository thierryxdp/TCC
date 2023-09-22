def faltante(L):
    ''' Dada uma lista de tamanho N-1, retorna um numero
    inteiro x que pertence ao intervalo [1,N] mas que nao
    pertence a lista de entrada
    list -> int'''
    contador = 0
    numeros = 1
    N = len(L) + 1
    lista_nova = []
    L.append(qualquer_numero)
    while numeros < N+1:
    	lista_nova.append(numeros)
		numeros +=1
	while contador < N:
		if lista_nova[contador] != L[contador]:
            return contador+1
        contador +=1