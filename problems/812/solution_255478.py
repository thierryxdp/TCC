def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    g=".","!","?","-",",",";",":"
    if g in f:
        return str.replace(f,str(g)," ")