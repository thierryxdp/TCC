def retira_pontuacao(frase):
    ''' Essa função retira toda pontuação e adiciona um espaço no local,
    depois retorna um a frase com as alterações'''
    if ':' in frase:
        frase= frase.replace(':',' ')
    if ',' in frase:
        frase= frase.replace(',',' ')
    if '.' in frase:
        frase= frase.replace('.',' ')
    if '!' in frase:
        frase= frase.replace('!',' ')
    if '?' in frase:
        frase= frase.replace('?',' ')
    if '-' in frase:
        frase= frase.replace('-',' ')
    if ';' in frase:
        frase= frase.replace(';',' ')
    return frase