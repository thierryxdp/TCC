def faltante(lista):
    """dada uma lista com N-1 elementos inteiros de 1 a N, a função
retorna o número que está faltando no intervalo.
list-->int

Parâmetros
lista: lista de tamanho N-1 de 1 a N"""
    indice=0
    while indice<len(lista):
        if lista[0]==2:
            return 1
        elif lista[indice]-1!=lista[indice-1] and lista[indice]>1:
                return lista[indice]-1
        indice=indice+1
    return lista[-1]+1