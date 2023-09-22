def total(lista,dic):
    """Funcao que define a soma dos produtos da lista de compras.
    list,dict->int"""
    soma = 0
    for lista in dic:
        soma += dic[lista]
    return round(soma,2)