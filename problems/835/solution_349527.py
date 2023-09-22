# Dada uma matriz com os tempos de 6 corredores
# para 10 voltas, queremos quem fez a melhor volta,
# com qual tempo e em que volta.
# Resolução:
# 1. Verifica a melhor volta de cada corredor;
# 2. Verifica, dentre a lista achada acima, a melhor volta;
# 3. Verifica, na lista de (1), o índice do valor encontrado
#    em (2) e soma 1: corredor;
# 4. Verifica, nos tempos do melhor corredor, em que volta foi melhor;
# 5. Devolve tupla contendo melhor volta, corredor e que volta.

def melhor_volta(tempos: list) -> tuple:
    '''Dada uma matriz com os tempos de 6 corredores
    para 10 voltas, retorna quem fez a melhor volta,
    com qual tempo e em que volta'''
    melhoresvoltas = []
    melhor = 0
    melhorvolta = 0
    corredor = 1
    volta = 1
    for corredor in tempos:
        melhor = min(corredor)
        melhoresvoltas += melhor
    melhorvolta = min(melhoresvoltas)
    corredor += list.index(melhoresvoltas, melhorvolta)
    volta += list.index((tempos[corredor - 1]), melhorvolta)
    return (corredor, melhorvolta, volta)