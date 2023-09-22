def maiores(lista:list, n:int) -> list:
    "Calcula e retorna uma lista de numeros inteiros maiores que n"
    "list, int -> list"
    lista.append(n)
    lista.sort()
    p= lista.index(n)
    return lista[p+1:]