def total(compras,catalogo):
    elemento = list(dict.keys(catalogo))
    valor = []
    for produto in (elemento):
        if produto in compras:
            a = dict.get(catalogo,produto)
            valor = list.append(valor, a)
   	return sum(valor)