def retira_pontuacao (frase):
    '''
       Dada uma frase a função returna a frase dada sem os 
       caracteres de pontuação
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
    if ',' in frase:
        str.replace(frase, ',', ' ')
    if '-' in frase:
        str.replace(frase, '-', ' ')
    if ':' in frase:
        str.replace(frase, ':', ' ')
    if ';' in frase:
        str.replace(frase, ';', ' ')
        return lista