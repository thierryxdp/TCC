def faltante(lista):
    """Função que recebe uma lista com N-1 inteiros numerados de 1 a N, retornando
    qual numero inteiro esta faltando nessa lista.
    entrada: lista
    retorno: int"""
    i=0
    while i < len(lista):
        if lista[i] > (i+1):
            return (i+1)
        i=i + 1
    return (i+1)