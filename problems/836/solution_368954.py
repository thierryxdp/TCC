def busca(setor,matriz):
    
    for i in matriz:
        for k in i[2]:
            lista=[]
            if k==setor:
                
                lista.append(i)
    return lista