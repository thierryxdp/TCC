def conta_numero(numero,matriz):
    '''recebe um numero inteiro e uma matriz de inteiros e retorna a qtd de vezes que ele aparece na matriz'''
    repete = 0
    for linha in matriz:
        repete = repete + list.count(linha,numero)
    return repete