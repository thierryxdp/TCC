def busca(matriz,string):
    lista=[]

    for i in range(len(matriz)):
        if matriz[i][2]==string:
            lista=lista+[[matriz[i][0],matriz[i][1],matriz[i][3]]]
            
    return lista