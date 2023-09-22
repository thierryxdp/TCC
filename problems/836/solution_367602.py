def busca(setor, matriz):
    contador = 0
    retorno = []
    while len(matriz) > contador:
        if setor in matriz[contador]:
            list.append(retorno, matriz[contador])
            for func in retorno:
                list.remove(func, setor)
    	contador = contador
    return retorno