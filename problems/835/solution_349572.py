def melhor_volta(matriz):
    '''dada uma matriz 6x10, retorna uma tupla informando
    de quem foia a melhor volta da prova, com qual tempo e em que volta
    list -> list'''
    
    lista=[0,0,0]
    lista_tempos=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista_tempos,matriz[i][j])
    minimo=min(lista_tempos)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==minimo:
                lista[0]=i+1
                lista[1]=matriz[i][j]
                lista[2]=j+1
    return tuple(lista)