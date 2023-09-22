def insere(lista_numero, n):
    n = (n,)
    list = lista_numero + (n,)
    list.join(",", list)
    list.sort(list)
    
    return list