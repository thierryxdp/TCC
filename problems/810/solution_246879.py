def retira_pontuacao(x):
    x = str.replace(x,'-',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,';',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    return x

def inverte(frase):
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return str.lower(retira_pontuacao(frase))