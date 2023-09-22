def total(lista_de_compras,produtos):
    """Função que, dada uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, retorna o valor total dos itens da lista que estejam disponíveis nesta loja; lista,dicionário->float"""
    
    soma = 0
    
    for x in lista_de_compras:
        
        if x in list(dict.keys(produtos)):
            
            soma = soma + produtos[x]
            
    return round(soma,2)