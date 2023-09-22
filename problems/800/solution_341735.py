def total(compras,catalogo):
    elemento = list(dict.keys(catalogo))
    valor = []
    for produto in (elemento):
        if produto in compras:
            valor = list.append(valor, (dict.get(catalogo),produto)
     return sum(valor)