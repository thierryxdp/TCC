def total(lista, valores):
    '''comentario padra
    e1, e2 -> s'''
    valor_total = 0.
    for item in lista:
        if item in valores:
	        valor_total += valores[item]
    return float(valor_total)