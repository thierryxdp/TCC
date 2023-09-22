def total(lista,dici):
    '''Recebe uma lista de compras e um dicionario
    contendo o preço de cada produto disponivel e retorna 
    o valor total da compra.
    list, dict -> int'''
    total = []
    for i in lista:
        if i in dici:
            total += sum[dici[i]]
    return total