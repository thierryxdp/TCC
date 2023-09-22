def retira_pontuacao(s):
    if(str.count(s,".")>0):
        v = str.replace(s,"."," ")
    if(str.count(s,",")>0):
        w = str.replace(v,","," ")
    if(str.count(s,";")>0):
        x = str.replace(w,";"," ")
    if(str.count(s,"!")>0):
        y = str.replace(x,"!"," ") 
    if(str.count(s,"-")>0):
        z = str.replace(y,"-"," ")
    return z