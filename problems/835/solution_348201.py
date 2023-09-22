def melhor_volta(matriz):
    """Função que receba uma matriz 6x10 e retorna uma tupla; list-> tuple"""
    t=(0,0,0)
    lista_t= []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista_t,matriz[i][j])
    m= min(lista_t)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i][j]==m:
                lista[0]=i+1
                lista[1]=matriz[i][j]
                lista[2]=j+1
    return [t]