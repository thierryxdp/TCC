def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        valor=min(lista)
        tupla=min(tupla)+(valor,)

    return tupla