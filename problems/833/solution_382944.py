'''Ao receber um número inteiro e uma matriz, o programa procura
pelo número na matriz, e retorna a quantidade de vezes
 que ele aparece '''

def conta_numero(numero, matriz):
    return list.count(matriz, numero)