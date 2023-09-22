def melhor_volta(matriz):
    """funcao calcula uma tupla informando a melhor volta da prova, com o tempo e 
    em que volta isso ocorre;
    list->tuple"""
    lista=[1,2,3]
    listaT=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.appen(listaT,matriz[i][j])
    mini=min(listaT)
    for i in range(len(matriz)):
        for j in range9len(matriz[0])):
            if matriz[i][j]==mini:
                lista[0]=i+1
                lista[1]=matriz[i][j]
                lista[2]=j+1
    return tuple(lista)