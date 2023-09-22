def retira_pontuacao(s):
    a = s
    str.replace(a,"-"," ")
    str.replace(a,":"," ")
    str.replace(a,";"," ")
    str.replace(a,","," ")
    str.replace(a,"."," ")
    str.replace(a,"!"," ")
    str.replace(a,"?"," ")
    return a