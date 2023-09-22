def retira_pontuacao(frase):
    a = str.replace(frase,".","")
    b = str.replace(a,"...","")
    c = str.replace(b,"!","")
    d = str.replace(c,";","")
    e = str.replace(d,":","")
    f = str.replace(e,"?","")
    g = str.replace(f,",","")
    h = str.replace(g,"-","")
    return a,b,c,d,e,f