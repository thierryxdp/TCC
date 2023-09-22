def retira_pontuacao(frase):
    '''
       Dada uma frase a função retorna a frase dada sem os
       caracteres de pontuação presentes na frase
       str -> str
    '''
    if '.' in frase:
        str.replace(frase, '.',' ')
    if '!' in frase:
        str.replace(frase, '!', ' ')
    if '?' in frase:
        str.replace(frase, '?', ' ')
    if '...' in frase:
        str.replace(frase, '...', ' ')
    if ',' in frase:
        str.replace(frase, ',', ' ')
    if ';' in frase:
        str.replace(frase, ';', ' ')
    if ':' in frase:
        str.replace(frase,':', ' ')
    if '-' in frase:
        str.replace(frase,'-', ' ')
        return frase