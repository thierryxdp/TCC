def retira_pontuacao(texto):
    s=str(texto)
    f=str.replace(s,"...",".") and str.replace(s,"."," ") and str.replace(s,"-"," ") and str.replace(s,":"," ") and str.replace(s,":"," ") and str.replace(s,","," ")
    return str(f)