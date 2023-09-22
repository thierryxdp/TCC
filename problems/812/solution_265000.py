from math import*

def retira_pontuacao(texto):
    x=str.replace(texto,'-',' ')
    y=str.replace(texto,',',' ')
    z=str.replace(texto,':',' ')
    w=str.replace(texto,';',' ')
    t=str.replace(texto,'.',' ')
    u=str.replace(texto,'!',' ')
    r=str.replace(texto,'?',' ')
    return x and y and z and w and t and u and r