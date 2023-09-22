def total (lista , dicionario):
    '''retorna o valor total de itens da lista que estão disponiveis 
    list,dict->float'''
    x=0
    for i in dicionario:
        if i in lista:
            x=x+(dict.get(dicionario,i))
    return round(x,2)