def melhor_volta(matriz):
    '''Esta função recebe uma matriz com os resultados do tempo de um circuito
percorridos por ateletas; ela retorna o melhor atleta, tempo e em que volta do
circuito.
list(list) --> tuple(int,float,int)
'''
    controle = []
    for corredor in matriz:
        list.append(controle,min(corredor))
    melhor_tempo = min(controle)
    melhor_corr = list.index(controle,min(controle))+1
    return melhor_corr, melhor_tempo, list.index(matriz[melhor_corr - 1],melhor_tempo)+1