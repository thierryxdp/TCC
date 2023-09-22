def faltante(lista):
    '''funcao que dada uma lista com N-1 inteiros enumerados de 1 a N, retorna qual o numero inteiro que esta faltando dentro desse intervalo
    lista->int'''
    lista1=lista[:]
    list.sort(lista1)
    i=0
    n=1 #o primeiro numero do intervalo [1,N]
    while i<len(lista):
    	if n in lista:
            n=n+1
    	i=i+1
    return n