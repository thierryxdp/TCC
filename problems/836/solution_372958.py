def busca(setor,matriz):
    lista_dados=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.append(lista_dados,matriz[i])
            lista_dados.remove(setor)
    return lista_dados