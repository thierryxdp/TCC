def conta_numero (numero: int, matriz: list)-> int:
    '''Dado um número e uma matriz, retorna quantas vezes esse número
    aparece na matriz'''
    cont = 0
    for i in range(len(matriz)):
        if numero in matriz[i]:
            cont += matriz[i].count(numero)
    return cont