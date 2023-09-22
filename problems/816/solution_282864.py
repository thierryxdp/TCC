def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    return (all(x>n for x in lista_numeros))