def busca(setor, matriz):
    lista=[]
    for i in matriz:
        if setor in i:
            lista=lista+[i[0], i[1], i[3]]
            
    return lista