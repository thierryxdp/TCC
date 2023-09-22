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
    x = str.split(x)
    x = list.reverse(x)
    return str.join(',',x)