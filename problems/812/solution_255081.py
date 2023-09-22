def retira_pontuacao(texto:str)->str:
    """Dado um determinado texto, retorna ele sem a pontuação comum à textos, como ponto final, vírgula, dois pontos, ponto e vírgula, ponto de exclamação, ponto de interrogação, travessão e reticências."""
    a=str.replace(texto,"-"," ")
    b=str.replace(a,"."," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"!"," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,","," ")
    return g