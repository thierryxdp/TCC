def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    j=str.replace(f,"-"," ")
    o=str.replace(j,"-"," ")
    g=str.strip(o,"?!.;:")
    return g[:]+" "