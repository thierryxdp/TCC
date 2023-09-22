def busca(matriz,nome):
    l=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if str.lower(nome) in str.lower(matriz[i][j]):
                list.append(l,matriz[j])
            l = l + matriz[j]     
    return l