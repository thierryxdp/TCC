def busca(setor, matriz):

        filtro = lambda linha: linha[2] == setor

        remove = lambda linha: linha.remove(2)

        lista = list(filter(filtro, matriz))

        lista = list(map(remove, lista))

        return lista