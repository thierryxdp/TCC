def busca(setor,matriz):
    lista_nova = []
    lista_final= []
    for i in range(len(matriz)):
        if matriz[i][2] in setor:
            lista_nova.append(matriz[i][0])
            lista_nova.append(matriz[i][1])
            lista_nova.append(matriz[i][3])
        	lista_final.append(lista_nova[i])
    return lista_final