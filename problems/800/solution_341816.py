def total(lista,preco):
    """Função qiue recebe uma lista de compras e um dicionário com preços do produtos de determinada loja e 
    retorna o valor total dos itens da lista que estejam disponieis na loja;
    list,dict-->float"""
    soma = 0
    for elem in lista:
        if elem in preco:
            soma = soma + preco[elem]
    return round(soma,2)