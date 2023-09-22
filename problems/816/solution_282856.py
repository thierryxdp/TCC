def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    lista_numeros.sort()
    filtro=filter(n>lista_numeros, lista_numeros)
    numeros_filtrados=list(filtro)
    return numeros_filtrados