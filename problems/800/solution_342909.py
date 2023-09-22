def total(lista_compras,dict_preco):
    '''
    dada uma lista contendo os ingredientes que deseja-se
    comprar e um dicionario onde as chaves sao os produtos
    disponiveis em um mercado e os valores associados as
    chaves são seus precos, retorna a quantidade de total
    que ira se gastar caso se compre no referido mercado
    dados de entrada: list, dict
    retorna: float
    '''
    total = o
    for i in lista_compras:
        if i dict.keys(dict_preco):
            total = total + dict_preco[i]
    return total