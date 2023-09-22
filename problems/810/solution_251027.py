def retira_pontuacao(x):
    travessao = str.replace(x,'-',' ')
    virgula = str.replace(travessao,',',' ')
    ponto = str.replace(virgula,'.',' ')
    exc = str.replace(ponto,'!',' ')
    interrog = str.replace(exc,'?',' ')
    retcs = str.replace(interrog,'...',' ')
    return retcs

def inverte(y):
    return list.reverse(y)