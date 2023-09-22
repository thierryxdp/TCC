from math import*

def retira_pontuacao(texto):
    x= str.replace(texto,'-',' ') str.replace(texto,',',' ') str.replace(texto,':',' ') str.replace(texto,';',' ') str.replace(texto,'.',' ')
    return x