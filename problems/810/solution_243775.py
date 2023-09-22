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
    x = retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    x = []
    x = list.reverse(x)
    return x