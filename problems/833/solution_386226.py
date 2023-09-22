def conta_numero(numero, matriz):
    """ Dado um número inteiro e uma matriz de inteiros de tamanho qualquer, 
    conta e retorna quantas vezes aquele número aparece na matriz 
    int, list(list) -> int """
    acumulador = 0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                acumulador+=1
    return acumulador