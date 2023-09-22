def maior_que_n(lista_numeros,n):
    return lista_numeros>n
def maiores(lista_numeros,n):
    "retorna uma lista com números maiores que n ordenados em ordem crescente"
    "list, int -> list"
    lista_numeros.sort()    
    filtro=filter(maior_que_n, lista_numeros)
    numeros_filtrados=list(filtro)
    return numeros_filtrados