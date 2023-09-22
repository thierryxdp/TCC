def total (compras, mercado):
    '''dados uma lista de compras e um dicionario contendo o preço de
    produto disponível em uma loja, retorna o valor total dos itens da 
    lista que estejam disponíveis na loja'''
    
    valor = 0
    
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)