def total(l_compras,dicio):
    '''
       funcao que retorna o valor total dos itens da lista
       de compras que estejam disponiveis na loja
       list, dict -> float
    '''
   
    produtos = list(dicio.keys())
    valores = list(dicio.values())
    soma = 0
    for el in l_compras:
        if el in produtos:
            soma = soma + valores[produtos.index(el)]
    return round(soma,2)