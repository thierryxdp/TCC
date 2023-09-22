def retira_pontuacao(frase):
    '''dsadadas'''
    if '.' in frase:
        fase=frase.replace('.', ' ')
    if '?' in frase:
        fase=frase.replace('?', ' ')
    if '-' in frase:
        fase=frase.replace('-', ' ')
    if ':' in frase:
        fase=frase.replace(':', ' ')
    if ';' in frase:
        fase=frase.replace(';', ' ')
    if '|' in frase:
        fase=frase.replace('!', ' ')