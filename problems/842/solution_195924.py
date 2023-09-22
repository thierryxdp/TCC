def classificacao(Cv, Ce, Cs, Fv, Fe, Fs):
    '''A FUNCAO CALCULA A CLASSIFICAÇAO DE UM CAMPEONATO E RETORNA AO MELHOR CLASSIFICADO'''
    Golmengo = (3*Cv) + Ce
    Golmintias= (3*Fv) + Fe
    if Golmengo > Golmintias:
        return 'Cormengo'
    if Golmengo < Golmintias:
        return 'Flaminthians'
    if Golmengo == Golmintias and Cs > Fs:
        return 'Cormengo'
    elif Golmengo == Golmintias and Fs > Cs:
         return 'Flaminthians'
    elif Golmengo == Golmintias and Cs == Fs:
         return 'Empate'