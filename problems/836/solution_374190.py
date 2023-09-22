def busca(string,matriz):
    
    registro=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] in string:
                matriz.remove(matriz[i][1])
                registro.append(matriz[i])

    return registro