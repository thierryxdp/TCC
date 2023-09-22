def conta_numero(numero,matriz):
    '''funcao que recebe um numero inteiro e uma matriz e conta quantas vezes esse numero aparece na matriz;
    int, list -> int'''
    quant_vezes = 0
    for numero in matriz[0]:
        quant_vezes += list.count(len(matriz[0]),numero)
    return quant_vezes