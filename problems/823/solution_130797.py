#list[int]->int
from random import randint
def faltante(lista):
    "Funçao que dada uma lista com N-1 inteiros numerados de 1 a N, descube qual número inteiro deste intervalo está faltando e retorna o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L." 
    pecas=len(lista)+1
    lista.sort()
    i=0
    while i<pecas:
        if i+1 not in lista:
            return i+1
        if lista[i] !=i+1:
            return i+1
        
    else:
        return i+= 1