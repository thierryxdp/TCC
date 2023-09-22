def maiores(lista:list, n:int) -> list:
    "Calcula e retorna uma lista de numeros inteiros maiores que n"
    "list, int -> list"
    lista.append(n)
    lista.sort()
    p= lista.index(n)
    return lista[p+1:]

def acima_da_media(lista:list, media:int) -> list:
    "Calcula e retorna uma lista da nota de alunos acima da media"
    "list, int -> list"
    lista.append(media)
    lista.sort()
    p= lista.index(media)
    return lista[p+1:]