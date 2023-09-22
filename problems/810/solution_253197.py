def retira_pontuacao(x):
    travessao = str.replace(x,'-',' ')
    virgula = str.replace(travessao,',',' ')
    ponto = str.replace(virgula,'.',' ')
    exc = str.replace(ponto,'!',' ')
    interrog = str.replace(exc,'?',' ')
    retcs = str.replace(interrog,'...',' ')
    return retcs

def inverte(x):
    return retira_pontuacao(str.lower(x[-1:]))