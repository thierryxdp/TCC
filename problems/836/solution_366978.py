def busca(setor,matriz):
    lista=[]
    for i in range(len(matriz)):
        qtd=list.count(matriz[i][2], setor)
        i+=1
        return qtd