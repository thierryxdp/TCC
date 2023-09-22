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

def inverte(texto):
    '''uma funcao que dada uma frase, retorna outra frase com as palavras da frase
    de entrada na ordem inversa, sem letras maiúsculas str -> str '''
    frase_em_minusculo = str.lower(retira_pontuacao(texto))
    palavras_splitadas = str.split(frase_em_minusculo)
    inverter = palavras_splitadas[::-1]
	concatena = str.join(' ', inverter,)
    return str(concatena)