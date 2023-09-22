def retira_pontuacao(x):
    x = str.replace(x,'...',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    x = str.replace(x,'-',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,';',' ')
    return x

def inverte(x):
    retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    list.reverse(x)
    x = ' '.join(x)
    return x