def melhor_volta(matriz):
    """A função recebe como entrada uma matriz 6 x 10 com
    os tempos em segundos dos corredores em cada volta. A
    função deve retornar uma tupla informando: De quem foi
    a melhor volta da prova, com qual tempo e em que volta.
    Sabendo que os corredores tem tempos diferentes. Considere
    os números de 1 a 6 para os corredores e de 1 a 10 as voltas.
    Entrada: List
    Saída: Tuple"""
    
    corridas=[]
    for corredor in matriz:
        menor_tempo=min(corredor)
        list.append(corridas,menor_tempo)
    indice=(list.index(corridas))min(corridas)
    volta=((list.index(matriz[indice]))(min(corridas,menores)))
    return tuple(indice+1,corridas[indice],volta+1)
    
    
    return tuple(