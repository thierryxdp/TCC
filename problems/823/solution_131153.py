#list[int]->int
def faltante(lista):
    "função que dada uma lista com N − 1 inteiros numerados de 1 a N, descobre qual número inteiro deste intervalo está faltando e retorna o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L." 
    lista.sort()
    posicao=0
    while posicao<len(lista):
        if lista[posicao]!=[posicao+1]:
            return posicao+1
        else :
            return posicao=posicao+1