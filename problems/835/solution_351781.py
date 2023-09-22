def melhor_volta(matriz):
    """Dada uma matriz 6 x 10 com os tempos em segundos de corredores em cada volta, retorna uma tupla com o corredor que obteve a melhpor volta da prova, em que tempo e em qual volta.
    list(lists) -> tuple"""
    x = []
    for i in matriz:
        list.append(x, min(i))
        a = list.index(x, min(x))
    b = list.index(matriz[a], min(x))    
    y = (a + 1, min(x), b + 1)    
    return y