def retira_pontuacao(frase):
    '''Função que retira a pontuação de uma frase, dentre
    os caracteres que ela retira estão inclusos: travessão,
    vírgula, dois pontos, ponto e vírgula e ponto final
    str -> str'''
    if '.' in frase:
        frase = str.replace(frase, '.', ' ')
    if ',' in frase:
        frase = str.replace(frase, ',', ' ')
    if '-' in frase:
        frase = str.replace(frase, '-', ' ')
    if ':' in frase:
        frase = str.replace(frase, ':', ' ')
    if ';' in frase:
        frase = str.replace(frase, ';', ' ')
    
    return frase