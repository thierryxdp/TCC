def total(lista,dicionario):
    '''Função que dada uma lista de compras e um dicionário contendo o preço de cada produto disponível, retorna o valor total dos itens da lista que estejam disponíveis;
       list,dicionario->float'''
    total = 0
    i = 0
    while i<len(lista):
        if lista[i] in dicionario:
            total = total + dict.get(dicionario,lista[i])
        i=i+1
    return round(total,2)