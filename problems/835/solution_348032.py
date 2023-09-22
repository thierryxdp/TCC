def melhor_volta(matriz):
    """dada uma matriz 6x10 representando 6 corredores em 10 voltas, determina qual corredor, em que volta teve o menor
    tempo
    :param matriz: lst(lst, ..., lst)
    :return: tup(int, float, int)
    """
    menor = volta = vencedor = 0

    for c in range(len(matriz)):
        if c == 0:
            menor = min(matriz[c])
            volta = matriz[c].index(min(matriz[c]))+1
            vencedor = c+1
        else:
            if min(matriz[c]) < menor:
                menor = min(matriz[c])
                volta = matriz[c].index(min(matriz[c]))+1
                vencedor = c+1
    return (vencedor, menor, volta)