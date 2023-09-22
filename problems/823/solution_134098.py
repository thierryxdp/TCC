def faltante(L):
    ''' Dada uma lista de tamanho N-1, retorna um numero
    inteiro x que pertence ao intervalo [1,N] mas que nao
    pertence a lista de entrada
    list -> int'''
    contador = 0
    numeros = 1
    N = len(L) + 1
    lista_nova = []
    while contador < N:
    	lista_nova.append(numeros)
        numeros +=1
	while contador < N:
        if lista_nova[contador] != L[contador]:
            return contador
        contador +=1