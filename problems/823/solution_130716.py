def faltante(L):
    '''Função que dada uma lista de tamanho N-1 com números inteiros
    de 1 a N, retorna o número que está faltando na sequência
    list -> int'''
    i = 0
    lista = list.sort(L)
    while i < len(lista):
        if lista[i] != i + 1:
            return lista[i] + 1