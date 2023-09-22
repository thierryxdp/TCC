def retira_pontuacao(s):
    i=0
    k=""
    while i<len(s):
        if(s[i] in "-,:;."):
        else:
            k=k+s[i]
    return k