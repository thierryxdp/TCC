def total(lista_de_compras,dicionario_produtos):
    '''Dado uma lista de compras e um dicionário de uma loja
    contendo os produtos disponíveis e seus preços, a função
    deve retornar o preço total dos itens da lista que tem 
    na loja;
    list,dict -> float'''
    valor_da_conta=0
    
    for i in dicionario_produtos:
        for i in lista_de_compras:
        valor_da_conta=+dict.get(dicionario_produtos,i)
        
    return (round(valor_da_conta,2))