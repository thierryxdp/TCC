def acima_da_media(lista):
    lista1 = []
    contador = 0
    tamanho = len(lista)
    media = sum(lista) // tamanho

    while contador <= tamanho:
        if lista[contador] >= media:
            lista1 = lista1 + [lista[contador]]
        contador = contador + 1
   
    return sorted(lista)