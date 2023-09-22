def inverte(f):
    s=str.split(f)
    list.reverse(s)
    str.join('.',s)
    return retira_pontuacao(s)