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

def inversa (texto:str)->str:
    """Dado um determinado texto, retorna o texto na ordem inversa e sem a pontuação"""
    a=str.split(retira_pontuacao())
    b=a[::-1]
    return str.join(b)