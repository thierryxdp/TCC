def melhor_volta(matriz):
    lista = []
    for i in range(6):
        for j in range(10):
            lista.append(min(matriz[i]))
            if matriz[i] in lista:
                c = list.index(lista,matriz[i])
                
    return (contador,min(lista),c)