def conta_numer(numero, matriz):
    ''' funcao que retorna a quantidade de numeros na matriz,
    dado numero inteiro e uma matriz
    int, list -> int'''
    ocorrencias = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == numero:
                ocorrencias = ocorrencias + 1
    return ocorrencias