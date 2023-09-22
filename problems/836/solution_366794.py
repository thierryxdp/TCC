def busca(setor, matriz):
    """essa função mostra as informações de fucionários dado o setor
str,list-->list"""
    lista = []
    for i in matriz:
        index1 = matriz.index(i)
        for j in i:
            index = matriz[index1].index(j)
            if setor == str(matriz[index1][index]):
                lista.append(matriz[index1][:2]+matriz[index1][3:])
    return(lista)