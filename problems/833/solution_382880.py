def conta_numero(numero, matriz):
    '''Função na qual dado um número inteiro n e uma matriz retorna
    o número de ocorrências deste número na matriz inserida. int, list
    -> int'''
    ocorrencias = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                ocorrencias += 1
    if len(matriz) == 0 or (len(matriz) == 0 and matriz = [[]]):
        return list.count(matriz[0], numero)
    return ocorrencias