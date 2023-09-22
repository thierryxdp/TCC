def busca(m, setor):
    encontra = []
    for i in range(len(m)):
        if str(setor) in m[i]:
            for j in range(len(m[0])):
                ficha=[]
                if  m[i][j] != str(setor):
                    ficha += m[i][j]
                    
                list.append(encontra, ficha)
    
    return encontra