def total(ls,d):
    """Função que recebe uma lista de compras e um dicionário com os preços de cada produto da lista e 
    retorna com a soma do valor total dos produtos"""
    sol = []
    for i in ls:
        if i in d:
            sol.append(d[i])
    return round(sum(sol),2)