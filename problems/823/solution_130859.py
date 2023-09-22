#list[int]->int
def faltante(lista):
    "função que dada uma lista com N − 1 inteiros numerados de 1 a N, descobre qual número inteiro deste intervalo está faltando e retorna o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L." 
    pecas=len(lista)+1
    lista.sort()
    i=0
    while i<pecas:
        if i+1 not in lista:
            return -1
        elif lista[i] != i+1:
            return i+1
        else :
            return i+1