def total(lista,dicio):
    '''recebe uma lista e um dicionario, retornando o valor
    total dos itens desejados
    list, dict -> int/float'''
    
    valores = []
    
    for item in lista:
        if item in dicio:
            list.append(valores,dict.get(item))
    return sum(valores)