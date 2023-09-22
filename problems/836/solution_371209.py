def busca(setor, matriz):

        filtro = lambda linha: linha[2] == setor

        remove = lambda linha: [linha[0], linha[1], linha[3]]

        lista = list(filter(filtro, matriz))

        lista = list(map(remove, lista))

        return lista