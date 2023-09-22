def conta_numero(numero,matriz):
    '''função que recebe um numero inteiro e uma matriz de inteiros e conta quantas vezes o numero aparece na matriz. int, list(list(int)) -> int'''
    quantidade = 0 
    for linha in matriz:
        qtd = qtd + list.count(linha,numero)
    return (qtd)