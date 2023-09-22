def busca(setor,matriz):
    lista=[]
    for i in matriz:
        if setor in matriz[i][2]:
            lista+=i
        
    return lista