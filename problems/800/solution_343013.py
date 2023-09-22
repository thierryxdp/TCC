def total(lista,dic):
    '''função que retorna o valor total dos itens da lista que estiverem no dicionário
    list, dic -> float'''
    k = 0
    for i in lista:
        if i in dic:
            k = k + dic[i]
    return round(k,2)