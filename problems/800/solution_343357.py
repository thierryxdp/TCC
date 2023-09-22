def total (lista_compras,dict_precos):
    valor_tot = 0
    contador = 0
    for contador in range(len(lista_compras)):
        if lista_compras[contador] in dict_precos:
            valor_tot = valor_tot + dict.get(dict_precos,lista_compras[contador])
        contador = contador + 1
    return round(valor_tot,2)