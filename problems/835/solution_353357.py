def melhor_volta(matriz):
    '''funçao que dada uma matriz 6x4 com os tempos em segundos dos corredores
em cada volta em cada volta, retorna uma tupla, com quem fez a volta mais rapida,
o tempo da volta  e em qual volta.
list -> tuple'''
    volta_rapida_piloto=[]
    for linha in matriz:
        volta_rapida_piloto.append(min(linha))
    volt_mais_rap=min(volta_rapida_piloto)
    for c in matriz:
        if volt_mais_rap in c:
            pilot_mais_rapid=matriz.index(c)+1
    for linha1 in matriz:
        for coluna in linha1:
            if coluna==volt_mais_rap:
                volta=linha1.index(coluna)+1
    return pilot_mais_rapid,volt_mais_rap,volta