def retira_pontuacao(frase):
    '''função que dada uma frase é retirada toda pontuação existente;
    str->str'''
    if '.' in frase:
        frase = str.replace(frase,'.',' ')
    if '-' in frase:
        frase = str.replace(frase,'-',' ')
    if '!' in frase:
        frase = str.replace(frase,'!',' ')
    if '?' in frase:
        frase = str.replace(frase,'?',' ')
    if ',' in frase:
        frase = str.replace(frase,',',' ')
    if ':' in frase:
        frase = str.replace(frase,':',' ')
    if '...' in frase:
        frase = str.replace(frase,'...',' ')
        return frase