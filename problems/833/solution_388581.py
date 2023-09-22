def conta_numero(numero,matriz):
    """funcao que dado um numero inteiro e uma matriz
    de inteiros de tamanho qualquer, retorna quantas
    vezes o numero aparece na matriz
    int,list->int"""
    lista = []
    for j in range(0,len(matriz)):
        for i in range(0,len(matriz[j])):
            if numero in matriz[j][i]:
                list.append(lista,numero)
    return len(lista)