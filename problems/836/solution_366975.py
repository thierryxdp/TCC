def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        qtd=list.count(matriz[i], setor)
        i+=1
        if qtd > 0:
            del matriz[i][2]
            return lista + [matriz[i]]
        else:
            return lista