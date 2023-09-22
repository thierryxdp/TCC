def busca(filtro,matriz):
    ponto= 0
    lista=[]
    for a in matriz:
        if filtro in matriz[ponto]:
            lista= lista+ matriz[ponto]
            
        ponto+= 1
    return [lista]