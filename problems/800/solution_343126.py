def total (lista_de_compras, produtos):
    
    contador = 0
    valor = 0
    
    for produtos in lista_de_compras:
        contador = contador + 1
        valor = valor + produtos[contador]
    if valor == len(produtos):
        return round(valor, 2)