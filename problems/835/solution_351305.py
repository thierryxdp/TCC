def melhor_volta(matriz):
    ''''''
    tup=()
    
    for lista in matriz:
        if lista in matriz:
            return min(lista)