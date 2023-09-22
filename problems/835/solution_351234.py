def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        if lista in matriz:
            tupla=tupla+[lista]
    return tupla