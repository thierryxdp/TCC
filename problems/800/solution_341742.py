def total(compras,catalogo):
    """A função faz o calculo total do valor das compras,
    com base na lista de compras e nos preços de uma loja.
    List,dict ---> Float"""
    elemento = list(dict.keys(catalogo))
    valor = 0
    for produto in (elemento):
        if produto in compras:
            valor = valor + dict.get(catalogo,produto)
    return sum(valor)