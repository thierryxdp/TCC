def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".")
    g=".","!","?","-",",",";",":"
    return str.replace(f,g," ")