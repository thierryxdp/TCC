def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    filtrado=[element for element in lista_numero if element > n]
    return filtrado