def conta_numero(numero,matriz):
    '''funcao que recebe como entrada um numero inteiro e uma matriz e retorna quantas vezes o numero de entrada aparece na matriz
    int, list(list) -> int'''
    contador=0
    for linha in matriz:
        for elemento in linha:
            if elemento==numero:
                contador+=1
    return contador