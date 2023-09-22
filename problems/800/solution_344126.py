def total(lista_de_compras, produtos):
    resultado=0
    for produto in lista_de_compras:
        resultado += produtos[produto]

    return resultado(round,2)