def total(lista, dicionario):
    """A função recebe como entrada uma lista de compras e um dicionário
    e retorna o valor total dos itens da lista presentes no dicionário.
    list, dict -> float"""
    
    soma = 0
    for item in lista:
        if item in dicionario:
            soma = soma + dicionario[item]
    return round(soma,2)