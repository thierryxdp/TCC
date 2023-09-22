def melhor_volta(matriz):
    ''''''
    tup=()
    
    for lista in matriz:
        valor=min(lista)
        tup=tup+valor
    return tup