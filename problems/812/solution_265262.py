def retira_pontuacao(s):
    v=str.replace(s,"."," ")
    w=str.replace(v,","," ")
    x=str.replace(w,";"," ")
    y=str.replace(x,"-"," ")
    z=str.replace(y,"?"," ")
    alpha=str.replace(z,"!"," ")
    return alpha