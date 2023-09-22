def conta_numero(numero:int,matriz:list)->int:
    '''Conta e retorna quantas vezes aquele 
    número aparece na matriz.'''
    contador = 0
    for i in matriz:
        contador += i.count(numero)
    return contador