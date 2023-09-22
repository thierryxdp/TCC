def inverte(retira_pontuacao):
    '''
    string -> string'''
    b = str.lower(retira_pontuacao)
    c = str.split(b)
    d = str.join(' ',c)
    return d