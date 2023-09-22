def retira_pontuacao(frase):
    '''A funcao recebe uma frase e substitui todos os seus sinais de pontuacao por
espacos str->str'''
    if '.' in frase:
        return frase.replace('.',' ',frase.count('.'))
    if '...' and '.' in frase:
        frase1=frase[0:frase.index('.')]
        frase2=frase[frase.index('.')+3:]
        return frase1+frase2
    if ',' in frase:
        return frase.replace(',',' ',frase.count(','))
    if ':' in frase:
        return frase.replace(':',' ',frase.count(':'))
    if '!' in frase:
        return frase.replace('!',' ',frase.count('!'))
    if '?' in frase:
        return frase.replace('?',' ',frase.count('?'))
    if ';' in frase:
        return frase.replace(';',' ',frase.count(':'))
    if '-' in frase:
        return frase.replace('-',' ',frase.count('-'))