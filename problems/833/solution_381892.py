def conta_numero(numero, matriz):
    """Função que recebe um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    retornando quantas vezes aquele numero aparece na matriz
    entrada: int, list(list)
    retorno: int"""
    qtas_vezes= 0
    for i in range(len(matriz)):
        soma= 0
        for j in range(len(matriz[0])):
            soma+= i.count(numero)
        qtas_vezes+= soma
    return qtas_vezes