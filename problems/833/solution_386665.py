def conta_numero(numero, matriz):
    '''retorna quantas vezes o numero aparece na matriz'''
    '''int,list[list] -> int'''
    vzes = 0 
    for i in range (len(matriz)):
        for j in (matriz[i]):
            if j ==numero:
                vezes=vezes - 1
        return vezes