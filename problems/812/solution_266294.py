def retira_pontuacao(frase):
    l = {'-':" ",',':" ",'.':" " ,';':" ",':':" ",'!':" ",'?':" "}
    for x in l:
        return str.replace(frase,x,l[x])