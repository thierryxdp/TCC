from math import*

def retira_pontuacao(texto):
    str.replace(texto,'-',' ')
    str.replace(texto,',',' ')
    str.replace(texto,':',' ')
    str.replace(texto,';',' ')
    str.replace(texto,'.',' ')
    str.replace(texto,'!',' ')
    str.replace(texto,'?',' ')