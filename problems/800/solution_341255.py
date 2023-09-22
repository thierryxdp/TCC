def total(lista,preco_produto):
    '''retorna o valor total dos itens da lista que estejam disponiveis na loja'''
    '''list, dict -> float'''
    valor=0
    i=0
    
    while lista[i] in preco_produto:
        valor=valor+preco_produto[lista[i]]
        i=i+1
        
        return valor