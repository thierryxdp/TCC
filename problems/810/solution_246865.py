def retira_pontuacao(x):
    x = str.replace(x,'-',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,';',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')

def inverte(y):
    y = retira_pontuacao(x)
    str.lower(y)
    str.split(y)
    return y