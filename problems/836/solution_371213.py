def busca_setor(lista):
    return lista[2]
def busca(matriz, setor):
    lista1 = list(map(busca_setor, range(len(matriz))))
    lista2 = filter(lambda i: setor1[i] == setor, i in range(len(lista1)))