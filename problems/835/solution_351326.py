def melhor_volta(matriz):
    ''''''
    tup=()
    
    for lista in matriz:
        for i in range(len(lista)):
            tup=i,lista[i]
    return tup