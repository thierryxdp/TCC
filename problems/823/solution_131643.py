def faltante(lista):
    lista_organizada = list.sort(lista)
    contador = 1
    peca_faltante = 0
    while contador < len(lista):
        if lista_organizada[contador] != (lista_organizada[contador - 1] + 1):
            peca_faltante = lista_organizada[contador]
    return peca_faltante