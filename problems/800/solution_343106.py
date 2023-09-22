def total(lista_compras,dicionario_precos):
    """
    Essa função, dados como argumentos uma lista contendo a lista de compras
    e um dicionario contendo o preço dos produtos, a função ira retornar o
    valor total das compras dos produtos disponiveis em uma determinada loja
    list,dict->float
    """
 
    itens_disponiveis = list(dict.keys(dicionario_precos))
    preco_produtos_dos_itens_disponiveis = []
    
    for item in itens_disponiveis:
        list.append(preco_produtos_dos_itens_disponiveis,dicionario_precos[item]

            
    return sum(preco_produtos_dos_itens_disponiveis)