def melhor_volta(matriz):
    ''''''
    tupla=()
    i=0
    for lista in matriz:
        menores=min(lista)
        tupla=(tupla)+(menores,)
        tempo=min(tupla)
    return tempo