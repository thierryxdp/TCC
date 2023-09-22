def busca(setor,matriz):
    retorno=[]
    for linha in range(len(matriz)):
        lista=[]
        if setor in matriz[linha]:
            lista.append(matriz[linha][0])
            lista.append(matriz[linha][1])
            lista.append(matriz[linha][3])
        	retorno.append(lista)
    return retorno