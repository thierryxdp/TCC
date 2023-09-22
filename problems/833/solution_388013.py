def conta_numero(numero, matriz):
    """ Função que dado um inteiro e uma matriz, 
    conta ae retorna quantas vezes aquele número aparece na matriz
    list, int -> int"""
    contador = 0
    for i in matriz:
        contador += i.count(numero)
    return contador