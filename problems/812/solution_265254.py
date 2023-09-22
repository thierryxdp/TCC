def retira_pontuacao(s):
    if(str.count(s,".")>0):
        x = str.replace(s,"."," ")
    if(str.count(s,",")>0):
        x = str.replace(s,","," ")
    if(str.count(s,";")>0):
        x = str.replace(s,";"," ")
    if(str.count(s,"!")>0):
        x = str.replace(s,"!"," ")
    if(str.count(s,"?")>0):
        x = str.replace(s,"?"," ")
    return x