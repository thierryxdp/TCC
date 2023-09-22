def total(compras,itens):
    
    '''Função que dada uma lista de compras
    e um dicionario de itens disponiveis na loja,
    retorna o valor total da compra.
    
    :param compras:str
    :return:float'''
    
    vtotal=0
    
    for item in range(len(itens)):
        if item in len(compras):
            vtotal=vtotal+sum(itens.values())