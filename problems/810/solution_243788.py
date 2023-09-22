def retira_pontuacao(x):
    x = str.replace(x,'-',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,';',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    return x
def lista(x):
    x = retira_pontuacao(x)
    x = str.lower(x)
    x = str.split(x)
    return x
def inverte(x):
    return list.reverse(lista(x))