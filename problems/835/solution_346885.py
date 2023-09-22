def melhor_volta(tempos):
    '''Dada uma matriz com os tempos de cada volta de
    uma corrida, retorna o corredor que obeteve a 
    melhor volta, qual foi o seu tempo e em qual volta;
    list -> tuple'''
    
    menoresTempos = []
    
    for volta in tempos:
        menoresTempos.append(min(volta))
    
    menorTempo = min(menoresTempos)
    
    voltaN = menoresTempos.index(menorTempo)
    corredor = tempos[voltaN].index(menorTempo)
    
    return (voltaN + 1, menorTempo, corredor + 1)