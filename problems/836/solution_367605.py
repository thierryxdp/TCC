def busca(setor, matriz):
    contador = 0
    contador1 = 0
    retorno = []
    while len(matriz) > contador:
        if setor in matriz[contador]:
            list.append(retorno, matriz[contador])
            while len(retorno) > contador1:
                list.remove(retorno[contador1], setor)
                contador1 = contador1 + 1
    	contador = contador + 1
    return retorno