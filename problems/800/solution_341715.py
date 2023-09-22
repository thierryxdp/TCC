def total(compras,catalogo):
    valor = []
    for produto in (catalogo):
        if dict.keys(catalogo) in compras[produto]:
            valor = list.append(valor, dict.values(catalogo))
    return sum(valor)