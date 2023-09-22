def melhor_volta(matriz):
    lista = []
    c = []
    for i in range(6):
        for j in range(10):
            lista.append(min(matriz[i]))
            if matriz[i] in lista:
                c = list.index(lista,matriz[i][j])
            tupla=(i+1,min(lista),j+1)    
    return tupla