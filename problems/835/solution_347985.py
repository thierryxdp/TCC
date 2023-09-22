def melhor_volta(matriz):
    lista = []
    c = 0
    for i in range(6):
        for j in range(10):
            lista.append(min(matriz[i]))
            if matriz[i] in lista:
                c = list.index(lista,matriz[i])
                
    return (min(lista),c)