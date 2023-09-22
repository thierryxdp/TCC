def retira_pontuacao(texto):
    ''' '''
    mod = str.replace(texto,'.',' ')
    mod = str.replace(mod,'...',' ')
    mod = str.replace(mod,'!',' ')
    mod = str.replace(mod,'?',' ')
    mod = str.replace(mod,',',' ')
    mod = str.replace(mod,'-',' ')
    mod = str.replace(mod,';',' ')
    mod = str.replace(mod,':',' ')
    return mod