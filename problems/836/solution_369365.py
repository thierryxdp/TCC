def busca(nome,matriz):
    novalis=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if nome in matriz[i]:
                list.remove(matriz,nome)
                list.append(novalis,matriz[i])
    return novalis