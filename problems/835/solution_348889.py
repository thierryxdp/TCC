def melhor_volta(matriz):
    '''funcao que dado lista com as voltas dos carros, retorna de quem foi a melhor volta,com que tempo e em que volta;list-->tuple'''
    lista=[]
    for i in range(len(matriz)):
        z=min(matriz[i])
        list.append(lista,z)
    menor=min(lista)
    quando=list.index(lista,menor) +1
    volta=list.index(matriz[quando-1],menor)+1
    return quando,menor,volta