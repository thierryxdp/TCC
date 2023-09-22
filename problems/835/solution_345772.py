def melhor_volta(matriz):
    """Função que dada uma matriz 6x10 com os tempos em segundos dos corredores em cada volta, retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta
       list -> tuple"""
    import math
    melhoresTempos = []
    for linha in matriz:
        menor = min(linha)
        melhoresTempos += [menor]
    melhorTempo = min(melhoresTempos)
    vencedor = list.index(melhoresTempos, melhorTempo) + 1
    volta = list.index(matriz[vencedor-1],melhorTempo) + 1
    return vencedor, melhorTempo, volta