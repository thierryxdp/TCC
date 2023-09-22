def faltante(lista):
    """Função que recebe uma lista com N-1 inteiros numerados de 1 a N, retornando
    qual numero inteiro esta faltando nessa lista.
    entrada: lista
    retorno: int"""
    i=0
    while i <= len(lista):
        if i== 0:
            if lista[i] > 1:
                return 1
            i=i + 1
        elif i == len(lista):
            return (lista[i] + 1)
        else:
            if (lista[i+1] - lista[i])!= 1:
            return (lista[i] + 1)
        else:
            i=i+1