from math import*

def retira_pontuacao(texto):
    x=str.replace(texto,'-',' ')
    y=str.replace(texto,',',' ')
    z=str.replace(texto,':',' ')
    w=str.replace(texto,';',' ')
    t=str.replace(texto,'.',' ')
    return x and y and z and w and t