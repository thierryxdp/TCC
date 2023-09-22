def melhor_volta(matriz):
    '''...'''
    
    lista=[0,0,0]
    lt=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lt,matriz[i][j])
    minimo = min(lt)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i][j] == minimo:
                lista[0] = i+1
                lista[1] = matriz[i][j]
                lista[2] = j+1
    return tuple (lista)