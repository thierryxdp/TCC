from math import*

def retira_pontuacao(texto):
    x=str.replace(texto,'-',' ')
    y=str.replace(texto,',',' ')
    w=str.replace(texto,':',' ')
    r=str.replace(texto,';',' ')
    u=str.replace(texto,'.',' ')
    t=str.replace(texto,'!',' ')
    q=str.replace(texto,'?',' ')
    return x or y or w or r or u or t or q