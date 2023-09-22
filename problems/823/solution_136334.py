def faltante(lista):
    '''recebe uma lista referente as peças de um quebra cabeças
    e retorna o numero da peça que falta.
    entrada: list
    saida: int'''
    posicao=0
    lista.sort()
    while posicao < len(lista):
        if (lista[posicao] - lista[posicao-1]) > 1:
            return lista[posicao]-1
        posicao = posicao + 1
    if 1 in lista:
        return len(lista) + 1
    else:
        return 1