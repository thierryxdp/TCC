def retira_pontuacao(f):
    x = str.replace(f,',',' ')
    y=str.replace(x,'-',' ')
    z=str.replace(y,':',' ')
    return z