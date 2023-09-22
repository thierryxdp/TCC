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
    str.lower(x)
    str.split(x)
    list.reverse(x)
    y = ' '.join(x)
    return y