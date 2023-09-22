def retira_pontuacao(x):
    '''s'''
    if '-' in x:
        return str.replace(x,'-',' ')
    if ',' in x:
        return str.replace(x,',',' ')
    if ';' in x:
        return str.replace(x,';',' ')
    if ':' in x:
        return str.replace(x,':',' ')
    if '.' in x:
        return str.replace(x,'.',' ')
    return x