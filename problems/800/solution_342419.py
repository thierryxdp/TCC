def total(lista,dic):
    """Função que recebe uma lista de compras e um dicionário
    contendo o preço de cada produto disponível e retorna o
    valor total dos itens da lista que estejam disponíveis na
    loja.
    list,dict->float."""
    soma=0
    for i in range(len(lista)):
        if lista[i] in dic.keys():
            soma=soma+dic[lista[i]]
    return round(soma,2)