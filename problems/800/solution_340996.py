def total(lista,dic):
    """essa função recebe uma lista de compras e um dicionário
    contendo vários produtos e seus preços. A função deve retornar
    a soma dos valores dos produtos citados na lista;
    list,dict-->float"""
    soma = 0 
    for c in lista:
        soma += dic[c]
    return round(soma,2)