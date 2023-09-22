def inverte(f):
    listap=str.split(retira_pontuacao(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte