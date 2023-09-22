def retira_pontuacao(frase):
    a='-'
    b=','
    c=':'
    d=';'
    e='.'
    f='?'
    g='!'
    iii='-,:;.?!...'
    for i in iii:
        h=frase.replace(iii,' ')
    return h