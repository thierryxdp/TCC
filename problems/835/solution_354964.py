def melhor_volta(tempos):
    melhor_corredor=0
    melhor_tempo=0
    volta=0
    for pos, corredor in enumerate(tempos):
        if pos==0:
            melhor_tempo=corredor[0]
        else:
            for volta, tempo in enumerate(corredor):
                if melhor_tempo>tempo:
                    melhor_tempo=tempo
                    melhor_corredor=pos+1
                    volta_do_melhor= volta+1
    return (melhor_corredor, melhor_tempo, volta_do_melhor)