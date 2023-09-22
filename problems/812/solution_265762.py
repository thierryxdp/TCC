def retira_pontuacao(x):
    virgula = str.replace(x,',','')
    ponto = str.replace(x,'.','')
    exc = str.replace(x,'!','')
    interrog = str.replace(x,'?','')
    retcs = str.replace(x,'...','')
    x = virgula, ponto, exc, interrog, retcs
    return x