# Dada uma lista e um número inteiro n,
# retorna todos da lista que são maiores que n
# list, int -> list
def maiores(lista, n):
    lista.append(n)
    lista.sort()
    indice = lista.index(n)
    return lista[indice + 1:]

# Dada uma lista de notas de uma turma,
# retorna uma lista ordenada com as notas que ficaram acima da média
# list -> list
def acima_da_media(lista):
    media = sum(lista) // len(lista)
    return maiores(lista, media)