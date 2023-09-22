def retira_pontuacao(x):
    x = str.replace(x,'-',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,';',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    return x
def inverte(x):
    x = str.lower(x)
    return x