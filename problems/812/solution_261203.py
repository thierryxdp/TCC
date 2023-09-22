def retira_pontuacao(x):
    if '-' in x:
        str.replace(x,'-',' ')
    if '.' in x:
        str.replace(x,'.',' ')
    if ';' in x:
        str.replace(x,';',' ')
    if ':' in x:
        str.replace(x,':',' ')
    if ', ' in x:
        str.replace(x,',',' ')
    if '!' in x:
        str.replace(x,'!',' ')
    if '?' in x:
        str.replace(x,'?',' ')
    return x