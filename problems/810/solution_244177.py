def retira_pontuacao(frase):
    a=str.replace(frase,',',' ')
    b=str.replace(a,'-',' ')
    c=str.replace(b,':',' ')
    d=str.replace(c,';',' ')
    e=str.replace(d,'...',' ')
    f=str.replace(e,'!',' ')
    g=str.replace(f,'?',' ')
    h=str.replace(g,'.',' ')
    return h

def inverte(frase):
    sem_pontuacao=retira_pontuacao(frase)
    lista=str.split(sem_pontuacao)
    list.reverse(lista)
    return ' ',join(lista)