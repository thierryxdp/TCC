def total(lista, dic):
    '''Retorna o valor da lista de compras
    	list, dict -> float'''
    soma = 0
    for item in lista:
        soma = soma + dic[item]
    return round(soma, 2)