def total(compras, precos):
    
    ''' Função que recebe uma lista de compras e 
        um dicionário com os preços dos produtos
        em uma certa loja e retorna o valor total dos
        itens da lista disponíveis na loja 
        list, dict -> float '''
    
    valor = 0
    
    for produto in compras and precos:
        valor = round(valor + precos[produto], 2)
        
    return valor