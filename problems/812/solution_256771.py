def retira_pontuacao(frase):
    '''Dada uma frase, retorna a mesma onde todos os caracteres de pontuacao foram substituidos por espacos.
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
    return frase