def retira_pontuacao(x):
    if '-' in x:
        str.replace(x,'-',' ')
    elif '.' in x:
        str.replace(x,'.',' ')
    elif ';' in x:
        str.replace(x,';',' ')
    elif ':' in x:
        str.replace(x,':',' ')
    elif ', ' in x:
        str.replace(x,',',' ')
    elif '!' in x:
        str.replace(x,'!',' ')
    elif '?' in x:
        str.replace(x,'?',' ')
    return x