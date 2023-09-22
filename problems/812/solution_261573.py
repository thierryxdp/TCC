retira_pontuacao(frase):
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