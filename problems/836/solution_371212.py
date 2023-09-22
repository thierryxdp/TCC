def busca_setor(lista):
    return lista[2]
def busca(matriz, setor):
    lista1 = list(map(busca_setor, range(len(matriz))))
    lista2 = filter(lambda setor1: setor1 == setor, range(len(lista1))