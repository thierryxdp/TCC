def retira_pontuacao(frase):
    '''uma funcao que substitui todos os caracteres de pontuacao de uma frase por
    espaco. str-> str'''
    afrase = str.replace(frase, '?', ' ')
    bfrase = str.replace(afrase, '-', ' ')
    cfrase = str.replace(bfrase, ',', ' ')
    dfrase = str.replace(cfrase, ':', ' ')
    efrase = str.replace(dfrase, ';', ' ')
    ffrase = str.replace(efrase, '.', ' ')
    
    frase_sem_pontuacao = str.replace(ffrase, '!', ' ')
    return frase_sem_pontuacao