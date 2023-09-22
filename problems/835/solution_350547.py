def melhor_volta(m):
    """Recebe uma matriz 6x10 com os tempos em segundo dos corredores a
    cada volta. Retorna uma tupla informando quem feez a 
    melhor volta e o tempo
    list-->tuple"""
    minimos=[]
    for jogador in m:
        minimos=minimos+min(jogador)
    vencedor=list.index(min(minimos), minimos)
	tempo= min(minimos)
    return [ vencedor, tempo]