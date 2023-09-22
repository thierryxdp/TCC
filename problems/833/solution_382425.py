def conta_numero(numero,matriz):
    '''Função que recebe um numero inteiro e uma matriz de 
    inteiros e conta quantas vezes o numero aparece na matriz.
    int, list(list(int)) -> int'''
    quantidade = 0
    
    for linha in matriz:
        quantidade = quantidade + list.count(linha,numero)
    
    return quantidade