def melhor_volta(matriz):
    '''retorna uma tupla com a melhor volta da prova, qual tempo e em que volta em uma matriz 6x10;
    matrz->tuple'''
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista,matriz[i][j])
    tempo=min(lista)
    pessoa=((list.index(lista,min(lista)))//10)+1
    volta=(list.index(lista,min(lista)))%6
    return (pessoa,tempo,volta)