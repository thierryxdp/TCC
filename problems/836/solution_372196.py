def busca(setor,matriz):
    matriz2=[]
    for i in matriz:
        lista=[]
        for j in i:
            if j ==setor:
                lista.append(i[0])
                lista.append(i[1])
                lista.append(i[3])
        if lista==[]:
            matriz2.append(lista)
    return matriz2