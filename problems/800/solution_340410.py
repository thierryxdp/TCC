def total(lista,d):
    '''retorna o somátorio dos valores do dicionário que 
    tenham suas respectivas chaves na lista; list, dict -> float'''
    samara = 0
    for i in range(len(lista)):
        if lista[i] in list(dict.keys(d)):
            samara += dict.get(d, lista[i])
    return round(samara, 2)