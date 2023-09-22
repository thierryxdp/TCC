def retira_pontuacao(pontuacao):
    e = str.replace(pontuacao, ".", " ")
    i = str.replace(e, "!", " ")
    o = str.replace(i, "?", " ")
    u = str.replace(o, ",", " ")
    a = str.replace(u,"-", " ")
    r = str.replace(a, ":", " ")
    s = str.replace(r,";", " ")
    
    return e + i + o + u + a + r + s