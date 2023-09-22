def retira_pontuacao(s):
    """A função que retira a pontuação de um texto
    str --> str"""
    v=str.replace(s,"."," ")
    w=str.replace(v,","," ")
    x=str.replace(w,";"," ")
    y=str.replace(x,"-"," ")
    z=str.replace(y,"?"," ")
    alpha=str.replace(z,"!"," ")
    return alpha