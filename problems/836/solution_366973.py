def busca(setor,matriz):
    lista=[]
    i=0
    while i < len(matriz):
        qtd=list.count(matriz[i], setor)
        i+=1
        if qtd > 0:
            list.remove(matriz[i][2])
            return lista + [matriz[i]]
        else:
            return lista