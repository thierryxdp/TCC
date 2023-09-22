def total(lista,dicionario):
    '''recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja,
    e retorna o valor total dos itens da lista que estejam disponíveis nesta loja
    list,dict-->int'''
    soma=0
    for i in lista:
        if i in dicionario:
            soma=soma+dicionario[i]
    a=round(soma,2)        
    return a