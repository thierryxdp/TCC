def melhor_volta(matriz):
    ''''''
    tupla=()
    
    for lista in matriz:
        valor=min(lista)
        tupla=(tupla)+(valor,)
        tempo=min(tupla)

    return tempo