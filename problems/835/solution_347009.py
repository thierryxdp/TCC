def melhor_volta(matriz):
    """Dada a matriz com as voltas dos corredores
    retorna o melhor colocado."""
    for i in matriz:
        lista = [list.pop(min(matriz))]
    return lista