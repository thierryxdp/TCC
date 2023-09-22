def melhor_volta(matriz):
    """Dada uma matriz 6x10 com tempos em seg, retorna uma
tupla que contém nome, tempo e volta do melhor colocado.
list -> tuple"""
    saida= (0,20,0)
    for i in range(6):
        for j in range(10):
            if matriz[i][j]<saida[1]:
                saida= (i+1,matriz[i][j],j+1)
    return saida