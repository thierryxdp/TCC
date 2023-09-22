def conta_numero(numero, matriz):
    '''Funcao que conta a quantidade
    com que um numero se repete ao longo da matriz'''
    '''List, int -> int'''
    contador = 0
    for i in matriz:
        contador += i.count(numero)
    return contador