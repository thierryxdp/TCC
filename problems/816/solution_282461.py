def maiores (lista_numeros, numero):
    list.sort(lista_numeros)
    indice = list.index(lista_numeros,numero)
    if numero > lista_numeros[indice]:
        return lista_numeros[indice:]