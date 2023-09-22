def faltante(pecas):

    list.sort(pecas)

    i = 0

    while i < len(pecas):
        if (pecas[i] - pecas[i+1]) != -1:
            return pecas[i]+1
		i = i + 1
    return pecas[len(pecas)]