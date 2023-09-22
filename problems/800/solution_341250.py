def total(lista,preco_produto):
    '''retorna o valor total dos itens da lista que estejam disponiveis na loja'''
    '''list, dict -> float'''
    valor=0
    i=0
    for produto[i] in lista:
        if produto in preco_produto:
            valor=valor+preco_produto[produto]
            i=i+1
            
            return valor