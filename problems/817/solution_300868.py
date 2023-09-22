def maiores(lista, n):
    """Esta funcao recebe uma lista com numeros inteiros, um numero n, e
    retorna outra lista que contem somente os numeros maiores que n da lista
    original.
    Entrada: list [int, int, int, ..., int]
    Saida: list [int, int, int, ..., int]"""
    list.append(lista, n)
    list.sort(lista)
    if not n==max(lista):
        return lista[list.index(lista, n)+1:]
    else:
        return []
    
def acima_da_media(notas):
    """Esta funcao recebe uma lista que contem varias notas de varios alunos e
    retorna outra lista que contem apenas notas acima da media.
    Entrada: list [float, float, float, ..., float]
    Saida: list [float, float, float, ..., float]"""
    media=sum(notas)/len(notas)
    return maiores(notas, media)