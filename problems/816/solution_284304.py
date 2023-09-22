def maiores(lista:list, n:int) -> list:
    "Calcula e retorna uma lista de numeros inteiros maiores que n"
    "list, int -> list"
    lista.sort()
    return lista[n:]