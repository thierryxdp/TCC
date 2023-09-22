def retira_pontuacao(frase):
    a = str.replace(frase,".","")
    b = str.replace(a,"...","")
    return b
    c = str.replace(b,"!","")
    return c
    d = str.replace(c,";","")
    return d
    e = str.replace(d,":","")
    return e
    f = str.replace(e,"?","")
    return f
    g = str.replace(f,",","")
    return g
    h = str.replace(g,"-","")
    return h