def retira_pontuacao(frase):
    '''Função que retira a potuação de uma frase dada. Dentre
    os caracteres que serão removidos estão: travessão, vírgula
    dois pontos, ponto e vírgula e pontos de encerramento de
    frase
    str -> str'''
    if '-' in frase:
        frase = str.replace(frase, '-', ' ')
    if ',' in frase:
        frase = str.replace(frase, ',', ' ')
    if ':' in frase:
        frase = str.replace(frase, ':', ' ')
    if ';' in frase:
        frase = str.replace(frase, ';', ' ')
    if '.' in frase:
        frase = str.replace(frase, '.', ' ')
    if '?' in frase:
        frase = str.replace(frase, '?', ' ')
    if '!' in frase:
        frase = str.replace(frase, '!', ' ')
    
    return frase