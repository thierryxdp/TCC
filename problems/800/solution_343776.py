def total(lista,dic):
    """Funcao que define a soma dos produtos da lista de compras.
    list,dict->int"""
    soma = 0
    for produto in lista:
        soma += dic[produto]
    return soma