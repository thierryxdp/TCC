def total(lista,dicio):
    '''
    Função que recebe como entrada uma lista de compras e um dicionário contendo o 
    preço de cada produto e retorna o valor total de todos os itens da lista.
    list,dict->float 
    '''
    valor=0
    i=0
    
    while i<len(lista):
        if lista[i] in dict.keys(dicio):
            valor=valor+dict.get(dicio,lista[i])
        i=i+1
    return round(valor,2)