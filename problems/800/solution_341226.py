def total(lista, dicionario):
    """Retorna o valor total dos itens da lista que estejam disponíveis nesta
       loja. list, dict-> float"""
    soma = 0
    for a in dicionario:
        if a in lista:
            soma = soma + dict.get(dicionario,a)
    return round(soma,2)