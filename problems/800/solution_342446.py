def total(lista,d):
    """dada a lista de compras, soma os valores dos itens."""
    soma = 0
    for item in lista:
        soma = soma + d[item]
    return round(soma,2)