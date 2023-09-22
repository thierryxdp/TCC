def retira_pontuacao(texto):
    '''funçao que retira as pontuações do texto e coloca um espaçao, str->str'''
    a=str.replace(texto,'.',' ')
    b=str.replace(a,'!',' ')
    c=str.replace(b,'?',' ')
    d=str.replace(c,'...',' ')
    e=str.replace(d,'-',' ')
    f=str.replace(e,',',' ')
    g=str.replace(f,':',' ')
    h=str.replace(g,';',' ')
    return h

def inverte(texto):
    '''função que inverte a frase, str-> str'''
    a=str.lower(retira_pontuacao(texto))
    b=str.split(a)
    list.reverse(b)
    return b