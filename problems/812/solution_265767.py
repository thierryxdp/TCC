def retira_pontuacao(x):
    travessao = str.replace(x,'-',' ')
    virgula = str.replace(travessao,',','')
    ponto = str.replace(virgula,'.','')
    exc = str.replace(ponto,'!','')
    interrog = str.replace(exc,'?','')
    retcs = str.replace(interrog,'...','')
    x = travessao, virgula, ponto, exc, interrog, retcs
    return retcs