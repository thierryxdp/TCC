def faltante(L):
    '''Função que dada uma lista com tamannho N - 1 contendo números inteiros
    e não repetidos de 1 a N, e retorna um número inteiro x que pertence
    ao intervalo [1,N] mas que não pertence a lista de entrada L;
    list -> int'''

    ordem = list.sort(L) 
    posicao = 0

    if L[0] != 1:
        return 1

    while L[posicao+1] == posicao+2:              
            posicao = posicao + 1          
           
    return L[posicao] + 1