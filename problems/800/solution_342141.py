def total(lista,preco):
    '''recebe uma lista de compras e um dicionario com
    o preco dos produtos e retorna o valor total dos itens
    disponiveis nessa loja
    list,dict->float'''
    valor=0
    for elemento in lista:
        if elemento in preco:
            valor=valor+preco[elemento]
    return round(valor,2)