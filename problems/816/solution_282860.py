def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    lista_numeros.sort()    
    lista_numeros=[n for n in lista_numeros if n>lista_numeros]
    return lista_numeros