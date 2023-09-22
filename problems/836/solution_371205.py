def busca(setor, matriz):

        filtro = lambda linha: linha[2] == setor

        lista = list(filter(filtro, matriz))

        return lista