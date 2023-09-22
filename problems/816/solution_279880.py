def maiores(lista_de_numeros: list,n: int) -> list:
    list.append(lista_de_numeros, n)
    list.sort(lista_de_numeros)
    del lista_de_numeros[:list.index(lista_de_numeros,n)]
    
    if list.index(lista_de_numeros,n) =< n:
        list.remove(lista_de_numeros, n)
    

    return lista_de_numeros