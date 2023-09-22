def busca(setor, matriz):

        filtro = lambda linha: linha[2] == setor

        lista = filter(map(filtro, matriz), True)

        return lista