def retira_pontuacao(frase):
    '''Função que retorna texto sem pontuação.
    str->str'''
    if '-'in frase:
        frase=str.replace(frase,'-',' ')
    if ',' in frase:
        frase=str.replace(frase,',',' ')
    if ':' in frase:
        frase=str.replace(frase,':',' ')  
    if ';' in frase:
        frase=str.replace(frase,';',' ')
    if '...' in frase:
        frase=str.replace(frase,'...',' ')
    if '?' in frase:
        frase=str.replace(frase,'?',' ')
    if '!' in frase:
        frase=str.replace(frase,'!',' ')
    if '.' in frase:
        frase=str.replace(frase,'.',' ')
    return frase