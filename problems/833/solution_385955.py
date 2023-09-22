ef conta_numero(numero, matriz):
    '''dado um numero e uma matriz calcula e retorna quantas vezes esse numero aparece na matriz
int,list->int'''
    i = 0
    contador = 0
    for x in matriz:
        contador = contador + list.count(matriz[i], numero)
        i = i + 1
    return contador