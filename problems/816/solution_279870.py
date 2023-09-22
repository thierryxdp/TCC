def maiores(lista_de_numeros: list,n: int) -> list:
    list.append(lista_de_numeros, n)
    list.sort(lista_de_numeros)
    del lista_de_numeros[:n-1]
    
    

    return lista_de_numeros