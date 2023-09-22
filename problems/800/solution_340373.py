def total(compras,precos):
    
    '''Função que recebe uma lista de compras e os preços dos produtos e retorna o total da compra. list,dict -> float'''

    total = 0
    
    for i in compras:
        if i in precos:
            total = total + dict.get(precos,i)
            
    return total