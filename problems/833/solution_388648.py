def conta_numero(numero,matriz):
    """funcao que dado um numero inteiro e uma matriz de 
    inteiros de tamanho qualquer, conta e retorna quantas
    vezes o numero dado aparece na matriz
    int,list->int"""
    lista = []
    for i in range(len(matriz)):
        if numero in matriz[i]:
            list.append(lista,numero)
    return len(lista)