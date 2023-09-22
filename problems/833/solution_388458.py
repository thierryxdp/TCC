def conta_numero(numero,matriz):
    '''função que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer retorna quantas vezes o numero aparece na matriz'''
    soma=0
    for linha in matriz:
        soma+=linha.count(numero)
    return soma