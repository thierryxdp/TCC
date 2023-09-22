def busca(setor,matriz):
    lista=[]
    for i in matriz:
        for k in i[2] :
            if k==setor:
                
            
               lista.append(k)
    return lista