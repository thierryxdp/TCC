def conta_numero(numero, matriz):
    """ a seguinte função reorna quantas vezes
    um númeromineteiro aparece na matriz
    int, list-> int"""
    
    quantidadenumeros=0
    
    for lin in range(len(matriz)):
        quantidade=list.count(matriz[lin], numero)
        quantidadenumeros = quantidadenumeros + quantidade
        return quantidadenumeros