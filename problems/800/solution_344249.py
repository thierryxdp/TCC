def total(lista, dic):
    """funcao que recebe uma lista de compras e um dicionário contendo o preco de cada produto disponível em uma determinada loja, e retorna o valor total dos ítens da lista que estejam disponíveis nesta loja;
    str->str"""
    valor=0
    for produto in range(len(lista)):
        
        x = lista[produto]
        if x in dict.keys(dic):
            valor+=dict.get(dic,x)
    return round (valor,2)