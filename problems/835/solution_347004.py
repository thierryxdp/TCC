def melhor_volta(matriz):
    """Dada a matriz com as voltas dos corredores
    retorna o melhor colocado."""
    tupla = ()
    for i in matriz:
        tupla.append(min(matriz[i]))
    return tupla