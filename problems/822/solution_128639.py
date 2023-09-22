def repetidos (lista):
    '''Retorna quantas vezes numa lista dois números consecutivos são iguais, lista -> int'''
    quant = len(lista)
    primeiro = lista[0]
    segundo = lista [1]
    resultado = 0
    while quant > 2:
        if primeiro == segundo:
            resultado = resultado + 1
        lista.pop(0)
    	quant == len(lista)
    return resultado