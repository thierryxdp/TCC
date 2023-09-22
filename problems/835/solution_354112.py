def melhor_volta(matriz):
    '''
    Função que dada uma matriz com os tempos dos corredores
    em segundos, retorna uma tupla com o corrdor que teve
    a melhor volta, o tempo feito por ele e qual foi a volta
    '''
    menor = volta
    volta= melhor 
    melhor = 1000
    for r in range(0, len(matriz)):
        for s in range(0, len(matriz[r])):
            if min(matriz[r][s], menor) == matriz[r][s]:
                menor=min(matriz[r][s], menor)
                melhor = r + 1
                volta = s + 1

    return melhor, menor, volta