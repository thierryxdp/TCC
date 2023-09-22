def total(lista, valores):
    '''comentario padra
    e1, e2 -> s'''
    valor_total = 0.
    for item in lista:
        valor_total += valores[item]
    return valor_total