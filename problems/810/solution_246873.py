def retira_pontuacao(s):
    i=0
    k=""
    while i<len(s):
        if(s[i] in "-,:;.?!"):
            k=k+" "
            i=i+1
        else:
            k=k+s[i]
            i=i+1
    return k.lower(len(k),0,-1)