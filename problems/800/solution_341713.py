def total(compras,catalogo):
    valor = []
    for produto in (catalogo):
        if compras[produto] in dict.keys(catalogo):
            lista = list.append(valor, dict.values(catalogo))
    return sum(valor)