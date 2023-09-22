def melhor_volta(matriz):
    lista = []
    c = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            lista.append(min(matriz[i]))
            if matriz[i] in lista:
                c = list.index(lista,matriz[i][j])
            tupla=(i+1,min(lista),j+1)    
    return tupla