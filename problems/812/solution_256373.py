def retira_pontuacao(frase):
    ''' essa funcao retorna uma frase dada na entrada sem pontuações '''
        if '.' in frase:
            frase = frase.replace('.',' ')
        if '_' in frase:
            frase = frase.replace('_',' ')
        if ',' in frase:
            frase = frase.replace(',',' ')
        if ':' in frase:
            frase = frase.replace(':',' ')
        if ';' in frase:
            frase = frase.replace(';',' ')
        if '?' in frase:
            frase = frase.replace('?',' ')
        if '!' in frase:
            frase = frase.replace('!',' ')
    return frase