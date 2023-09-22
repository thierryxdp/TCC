def total(lista, produtos):
    """A função retorna o valor total dos itens da lista que estejam
    disponíveis nesta loja.
    list--dict-->int."""
    i = 0
    final = 0

    for x in lista:
        if lista[i] in produtos:
            final+= produtos[lista[i]]
            i+=1
    return round(final,2)