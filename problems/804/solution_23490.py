def filtrar_pares(tupla):
    '''função que recebe como entrada uma lista de 4 números int e monta um conjunto apenas com os números pares e dá o resultado convertido em tupla.'''
    pares=[]
    for x in tupla:
        if x%2==0:
            pares.append(x)
    pares=tuple(pares[:])
    return pares