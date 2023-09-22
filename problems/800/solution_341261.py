def total(lista,preco_produto):
    '''retorna o valor total dos itens da lista que estejam disponiveis na loja'''
    '''list, dict -> float'''
    
    soma=0
    
    for produto in lista:
        if produto in preco_produto:
            soma=soma+preco_produto
            
            return soma