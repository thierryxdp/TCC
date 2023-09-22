def maiores(lista_de_numeros, n):
    lista_de_numeros[0:0] = [n]
    list.sort(lista_de_numeros)
    
    return lista_de_numeros