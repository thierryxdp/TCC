def retira_pontuacao(x):
    l=['.',',','!','?',':',";"]
    for y in l:
        s=str.replace(x,l," ")
        return s