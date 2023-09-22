def conta_numero(numero,matriz):
    '''funcao que recebe um numero inteiro e uma matriz e conta quantas vezes esse numero aparece na matriz;
    int, list -> int'''
    quant_vezes = 0
    for i in matriz:
        for numero in i:
            quant_vezes += list.count(i,numero)
    return quant_vezes