def total(compras,dicionario):
    '''Função que recebe uma lista de compras e um dicionário com o preço
    de cada produto e retorna o valor total dessa lista (soma dos preços)
    
    list,dict->float'''
    
    soma = 0
    
    for contador in compras:
        soma = soma + dicionario[contador]
    
    return round(soma,2)