def total(lista_de_compras,dicionario_produtos):
    '''Dado uma lista de compras e um dicionário de uma loja
    contendo os produtos disponíveis e seus preços, a função
    deve retornar o preço total dos itens da lista que tem 
    na loja;
    list,dict -> float'''
    valor_da_conta=0
    
    for i in len(lista_de_compras):
        x=lista_de_compras[i]
        if x in dict.keys(dicionario_produtos):
        valor_da_conta=valor_da_conta+ dict.get(dicionario_produtos,i)
        
    return (round(valor_da_conta,2))