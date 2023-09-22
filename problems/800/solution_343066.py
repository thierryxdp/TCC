def total(prod,valor):
    '''
    Função que recebe uma lista de produtos e um dicionário
    contendo produtos como chaves e o preço  referentes aos
    mesmos como valores e retorna o total da compra dos itens
    informados na lista.
    
    list, dic -> float
    '''
    total_da_conta = 0
    
    for i in range(0,len(prod)):
        if prod[i] in valor:
            valProd = valor.get(prod[i])
            total_da_conta = total_da_conta + valProd
            
    return round(total_da_conta,2)