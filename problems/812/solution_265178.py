def retira_pontuacao (frase):
    '''
       Dada uma frase retorna a mesma frase sem os caracteres
       de pontuação que apresentava a frase de entrada
       str -> str
    '''
    if '.' in frase:
        str.replace(frase, '.', ' ')
    if '!' in frase:
        str.replace(frase, '!', ' ')
    if '?' in frase:
        str.replace(frase, '?', ' ')
    if '...' in frase:
        str.replace(frase, '...', ' ')
    if '-' in frase:
        str.replace(frase, '-', ' ')
    if ',' in frase:
        str.replace(frase, ',', ' ')
    if ':' in frase:
        str.replace(frase, ':', ' ')
    if ';' in frase:
        str.replace(frase, ';', ' ')
    return frase