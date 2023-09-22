def total(lista, dicionario):
    acumulador = 0
    contador = 0
    for numero in range(len(lista)):
        compra = lista[contador]
        valor = dict.get(dicionario, compra)
        acumulador = acumulador + valor        
        contador = contador + 1   
    return round(acumulador, 2)