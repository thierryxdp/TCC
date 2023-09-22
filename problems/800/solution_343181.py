def total(L,D):
    '''Funcao que recebe uma lista de compras e um dicionario com
    o valor dos objetos no mercado e retorna o valor total da compra
    list, dict -> float
    '''
    valor = 0
    for x in range(len(L)):
        valor += D[L[x]]
    return round(valor,2)