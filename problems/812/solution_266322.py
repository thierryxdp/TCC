def retira_pontuacao(x):
    l=[',','.','!','?',':',";"]
    for y in l:
        s=str.replace(x,y," ")
        return s