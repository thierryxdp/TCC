def busca(setor,m):
    lista=[]
    for i in range(len(m)):
        if setor in m[i][2]:
            del m[i][2]
            list.append(lista,m[i])
    return lista