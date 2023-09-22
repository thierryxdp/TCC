def retira_pontuacao(a):
    a=str.replace(a,","," ")
    a=str.strip(a,"?")
    a=str.strip(a,"!")
    return a