def melhor_volta(tempos):
    '''funcao que informa quem foi a melhor volta da prova, com qual tempo e em qual volta'''
    corredor_mais_rapido=0
    melhor_tempo=0
    volta=0
    for pos, corredor in enumarate(tempos):
        if pos==0:
            melhor_tempo==corredor[0]
        else:
            for volta, tempo in enumarate(corredor):
                if melhor_tempo>tempo:
                    melhor_tempo=tempo
                    corredor_mais_rapido=pos+1
                    volta_melhor=volta+1
    return (corredor_mais_rapido, melhor_tempo, volta_melhor)