def total(lista,dic):
    """Funcao que define a soma dos produtos da lista de compras.
    list,dict->int"""
    i = 0
    soma = 0
    for lista[i] in dic:
        soma += dic[lista[i]]
    i = i + 1
    return round(soma,2)