def busca(setor,matriz):
    banco= []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            x= matriz[i][0:2] + matriz[i][3:]
            list.append(banco,x)
    return banco