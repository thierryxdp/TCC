def total(listas=[],dict={}):
    ''' funcao que recebera uma lista de comprar e um dicionario contendo
    o preco dos produtos disponiveis na loja e retornara o valor total
    de todos os itens da lista da lista que estao disponiveis na loja'''
    cont = 0
    for i in listas:
        cont+=didct[i]
        return round (cont,2)