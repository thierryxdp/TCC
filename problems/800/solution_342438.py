def total(lista_compras,preco_produtos):
    """Essa função receberá como parâmetro de entrada uma
    lista de compras e um dicionário contendo o preço de 
    cada produto disponível em uma determinada loja. Posto
    isso, tal função retornará o valor total dos itens da
    lista que estejam disponíveis na loja em questão.
    
    Obs: O resultado que será retornado deve conter somente
    duas casas decimais.
    
    list, dict -> float
    """
    
    Valor_Total_ProdutosDisponiveis = 0
    for i in lista_compras:
        if i in preco_produtos:
            n = dict.get(preco_produtos, i)
        Valor_Total_ProdutosDisponiveis =  Valor_Total_ProdutosDisponiveis + n
    return Valor_Total_ProdutosDisponiveis