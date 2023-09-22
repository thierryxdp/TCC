def melhor_volta(matriz):
    """Funcao que recebe uma matriz de 6x10 com os tempos em segundos dos corredores
    em cada volta, retorna uma tupla informando de quem foi a melhor volta da prova e com qual tempo
    matriz -> tulpa"""
    i=0
    l=[]
    for i in matriz:
        rapido=min(i)
        l.append(rapido)
    melhor_volta=min(l)
    vencedor+=l.index(melhor_volta)
    volta+=matriz[vencedor].index(melhor_volta)
    return melhor_volta, vencedor, volta