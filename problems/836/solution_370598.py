def busca(setor,mat):
    matriz=[]
    for i in mat:
        lista=[]
        for j in i:
            if j == setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
        if lista!=[]:
            matriz.append(lista)
    return matriz