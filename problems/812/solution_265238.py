def retira_pontuacao(a):
    s=list(a)
    str.replace(s,"-"," ")
    str.replace(s,":"," ")
    str.replace(s,";"," ")
    str.replace(s,","," ")
    str.replace(s,"."," ")
    str.replace(s,"!"," ")
    str.replace(s,"?"," ")
    return s