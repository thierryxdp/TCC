def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    quant = len(lista)
    resultado = 0
    while quant > 1:
        if lista[0] == lista [1]:
            resultado = resultado + 1
        del(lista[0])
        quant == len(lista)
    return resultado