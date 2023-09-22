def total(l_compras,dicio):
    produtos = list(dicio.keys())
    valores = list(dicio.values())
    soma = 0
    for el in l_compras:
        if el in produtos:
            soma = soma + valores[produtos.index(el)]
    return soma