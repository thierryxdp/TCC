def melhor_volta(matriz):
    ''''''
    tup=()
    
    for lista in matriz:
        if lista in matriz:
            a=min(lista[0]),min(lista[1])
            return a