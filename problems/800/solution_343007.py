def total(l,d):
    '''compara os itens de uma lista com os de um dicionario
    e soma os valores dos itens que sao comuns entre os dois
    list, dict -> float'''
    t=0
    for x in l:
        if x in d:
            t=t+d[x]
    return round(t,2)