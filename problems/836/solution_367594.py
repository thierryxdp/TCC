def busca(setor, matriz):
    contador = 0
    retorno = []
    while len(matriz) > contador:
        if setor in matriz[contador]:
            list.append(retorno, matriz[contador])
    	contador = contador + 1
    list.remove(retorno, setor)
    return retorno