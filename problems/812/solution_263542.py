def retira_pontuacao(frase):
    '''
       Funcao que retorna a frase onde todos os caracteres
       de pontuacao tenham sido substituidos por espaco
       str -> str
    '''
    if '-' in frase:
        frase = frase.replace('-',' ')
    if ',' in frase:
        frase = frase.replace(',',' ')
    if ':' in frase:
        frase = frase.replace(':',' ')
    if ';' in frase:
        frase = frase.replace(';',' ')
    if '.' in frase:
        frase = frase.replace('.',' ')
    if '!' in frase:
        frase = frase.replace('!',' ')
    if '?' in frase:
        frase = frase.replace('?',' ')
    if '...' in frase:
        frase = frase.replace('...',' ')

        return frase