def conta_numero(numero, matriz):
    '''funcao que dado um numero inteiro e uma matriz, retorna a quantidade de vezes que o numero repetiu; matriz -> int'''
    i = 0
    for linha in matriz:
        i = i + list.count(numero, linha)
    return i