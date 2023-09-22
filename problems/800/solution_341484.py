def total(lista, produtos):
    '''função que recebe uma lista de compras e um dicionário
    contendo o preço desses itens numa loja, e retorna o preço
    total da compra
    valor de entrada: lista, dicionário
    valor de saída: float'''
    valor=0
    for i in lista:
        if i in produtos:
            valor=valor+produtos[i]
    return round(valor,2)