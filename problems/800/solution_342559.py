def total(lista_de_compras,dicionario):

    type(lista_de_compras)== list
    type(dicionario)==dict
	total = 0
    for item in lista_de_compras:
        if item in dicionario.keys():
            total += dicionario[item]
    return total