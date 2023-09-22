def maiores (lista_numeros, numero):
    list.sort(lista_numeros)
    if numero > lista_numeros[list.index(lista_numeros,numero)]:
        return lista_numeros[list.index(lista_numeros,numero):]