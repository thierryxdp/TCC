def total(compras,mercado):
    
    '''Função que dada uma lista de compras
    e um dicionario de itens disponiveis na loja,
    retorna o valor total da compra.
    
    :param compras:str
    :param mercado:dict
    :return:float'''
    
    vtotal=0
    
    for item in range(len(compras)):
        if compras[item] in mercado.keys():
            vtotal=vtotal+sum(mercado.values())
    return vtotal