def busca(setor,matriz):
    contador=0
    retorno = []
    posicao=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == setor:
                contador=contador+1
                list.append(retorno,i)
    return retorno