def retira_pontuacao (x):
    y= str((list.reverse(list[x]))
    
    if "-" in x:
        y = str.replace(x,"-"," ",str.count(x,"-"))
    if "," in x:
        y = str.replace(x,","," ",str.count(x,","))
    if ":" in x:
        y =  str.replace(x,":"," ",str.count(x,":"))
    if ";" in x:
        y =  str.replace(x,";"," ",str.count(x,";"))
    if "!" in x:
        y =  str.replace(x,"!"," ",str.count(x,"!"))
    if "?" in x:
        y =  str.replace(x,"?"," ",str.count(x,"?"))
    if "." in x:
        y =  str.replace(x,"."," ",str.count(x,"."))
    return y