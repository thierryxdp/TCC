def retira_pontuacao(frase):
    '''A funcao recebe uma frase e substitui todos os seus sinais de pontuacao por
espacos str->str'''
    if '.' in frase:
        return frase.replace('.',' ')
    if ',' in frase:
        return frase.replace(',',' ')
    if ':' in frase:
        return frase.replace(':',' ')
    if '!' in frase:
        return frase.replace('!',' ')
    if '?' in frase:
        return frase.replace('?',' ')
    if ';' in frase:
        return frase.replace(';',' ')
        frase6=parte1+' '+parte2
    if '-' in frase:
        return frase.replace('-',' ')