def total(ls,d):
    """Essa questão serve para calcular o total do valor de itens, de acordo com
    uma lista de compras e um dicionário com os preços
    list, dict->float"""
    soma = 0
    for item in ls:
        soma = soma + d[item]
    return round(soma,2)