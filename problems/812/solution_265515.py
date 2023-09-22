def retira_pontuacao(frase):
    s=str.replace(frase, ".", " ")
    t=str.replace(s, "," , " ")
    w=str.replace(t, ":", " ")
    u=str.replace(w, "!", " ")
    p=str.replace(u, "!", " ")
    m=str.replace(p, "?", " ")
    L=str.replace(m, "-", " ")
    return L