def melhor_volta(matriz):
    ''''''
    tup=()
    
    for lista in matriz:
        for i in range(len(lista)):
            tup=tup/lista[i]
    return tup