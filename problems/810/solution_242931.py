def retira_pontuacao(x):
    x = str.replace(x,'-',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,';',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    return x
def inverte(y):
    y = str.lower(y)
    return y