def busca(nome,matriz):
    novalis=[]
    for i in range(len(matriz)):
        if nome in matriz[i]:
            list.remove(matriz[i],nome)
            list.append(novalis,matriz[i])
    return novalis