def retira_pontuacao(x):
    '''s'''
    if '-' in x:
        return str.replace(x,'-',' ')
    elif '.' in x:
        return str.replace(x,'.',' ')
    elif ';' in x:
        return str.replace(x,';',' ')
    elif ':' in x:
        return str.replace(x,':',' ')
    elif ', ' in x:
        return str.replace(x,',',' ')
    elif '!' in x:
        return str.replace(x,'!',' ')
    return x