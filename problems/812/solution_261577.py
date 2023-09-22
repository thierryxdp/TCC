def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase sem pontuação alguma.
    str->str"""
    x=frase
    if '-' in x:
        x=str.replace(x,'-',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if '.' in x:
        x=str.replace(x,'.',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '!' in x:
        x=str.replace(x,'!',' ')
    if '...' in x:
        x=str.replace(x,'...',' ')
    return x