def melhor_volta(matriz):
    """Funcao que, ao receber uma matriz 6x10 com os tempos em segundos dos corredores em cada uma das voltas, retorna uma tupla informando de quem foi a melhor volta, com que tempo e em que volta
    list -> tuple"""
    minimos=[]
    for a in range(len(matriz)):
        list.append(minimos,min(matriz[a]))
    m=min(minimos)
    n=list.index(minimos,m)+1
    f=list.index(matriz[n-1],m)+1
    return (n,m,f)