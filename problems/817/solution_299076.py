def maiores(lista:list, n:int) -> list:
    "Calcula e retorna uma lista de numeros inteiros maiores que n"
    "list, int -> list"
    lista.append(n)
    lista.sort()
    p= lista.index(n)
    return lista[p+1:]

def acima_da_media(notas:list[float]) -> list[float]:
    "Calcula e retorna uma lista da nota de alunos acima da media"
    "list -> list"
    media = sum(notas)/len(notas)
    acimaDaMedia = maiores(notas, media)
    if len(notas) != 1:
    	return acimaDaMedia
    else:
        return list()