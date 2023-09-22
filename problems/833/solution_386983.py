def conta_numero(numero:list, matriz:int)->int:
    '''Retorna quantas vezes um mnúmero aparece na matriz'''
    contador= 0 
    for i in matriz:
        contador = contador + i.count(numero)
    return contador