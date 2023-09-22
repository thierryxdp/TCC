def total(lista,preco_produto):
    '''retorna o valor total dos itens da lista que estejam disponiveis na loja'''
    '''list, dict -> float'''
    
    valor=0
    
    for produto in lista:
        if produto in preco_produto:
            valor=valor+preco_produto
            
            return valor