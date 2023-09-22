def total(l_compras,dicio):
    '''
       funcao que retorna o valor total dos itens da lista
       de compras que estejam disponiveis na loja
       list, dict -> float
    '''
    39.59999999999999 = 39.6
    produtos = list(dicio.keys())
    valores = list(dicio.values())
    soma = 0
    for el in l_compras:
        if el in produtos:
            soma = soma + valores[produtos.index(el)]
    return soma