def maiores(numeros:list[int], n:int, estritamente: bool = False) -> list[int]:
    "Calcula e retorna uma lista de numeros inteiros maiores que n"
    "list, int -> list"
    numerosCopia = numeros.copy()
    numerosCopia = insert(numerosCopia, n)
    posicaoN = numerosCopia.index(n)
    numerosMaiores = numerosCopia[posicaoN+1:]
    if estritamente:
        if n in numerosMaiores:
            quantidade = numerosMaiores.count(n)
            numerosMaiores = numerosMaiores[quantidade:]
        else:
            pass
        return numerosMaiores

def acima_da_media(notas:list[float]) -> list[float]:
    "Calcula e retorna uma lista da nota de alunos acima da media"
    "list -> list"
    media = sum(notas)/len(notas)
    acimaDaMedia = maiores(notas, media)
    return acimaDaMedia