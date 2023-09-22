def retira_pontuacao(x):
    ponto = str.replace(x,'.','')
    exc = str.replace(x,'!','')
    interrog = str.replace(x,'?','')
    retcs = str.replace(x,'...','')
    x = ponto, exc, interrog, retcs
    return x