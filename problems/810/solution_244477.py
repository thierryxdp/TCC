def tira_pontuacao(x):
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
    y = tira_pontuacao(x)