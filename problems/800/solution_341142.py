def total(lista_de_compras,preco_produtos):
    '''funcao que recebe uma lista de compras o dicionario preco_produtos contendo o valor de cada produto disponivel na loja e retorna o valor total de itens da lista que estejam disponiveis na loja
    list, dict -> int'''
    valor=0
    for produto in lista_de_compras:
        if produto in preco_produtos:
            valor=valor+dict.get(preco_produtos,,produto)
    return valor