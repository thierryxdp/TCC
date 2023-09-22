def busca(setor, matriz):
    contador = 0
    retorno = []
    while len(matriz) > contador:
        if setor in matriz[contador]:
            list.append(retorno, matriz[contador])
            list.remove(retorno[contador], setor )
    	contador = contador + 1
    return retorno