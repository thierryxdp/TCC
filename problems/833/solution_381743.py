def conta_numero(numero,matriz):
    ''' função que procura e calcula a quantidade de aparições
        do número fornecido dentro da matriz de entrada
        [int,list--> int]'''

    soma = 0
    for sublista in matriz:
        for inteiro in matriz:
            if inteiro == numero:
                soma += 1
    return soma