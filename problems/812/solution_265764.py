def retira_pontuacao(x):
    virgula = str.replace(x,',','')
    ponto = str.replace(virgula,'.','')
    exc = str.replace(ponto,'!','')
    interrog = str.replace(exc,'?','')
    retcs = str.replace(interrog,'...','')
    x = virgula, ponto, exc, interrog, retcs
    return retcs