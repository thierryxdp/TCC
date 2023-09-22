def retira_pontuacao (x):
    
    if "-" in x:
        x = str.replace(x,"-"," ",str.count(x,"-"))
    if "," in x:
        x = str.replace(x,","," ",str.count(x,","))
    if ":" in x:
        x =  str.replace(x,":"," ",str.count(x,":"))
    if ";" in x:
        x =  str.replace(x,";"," ",str.count(x,";"))
    if "!" in x:
        x =  str.replace(x,"!"," ",str.count(x,"!"))
    if "?" in x:
        x =  str.replace(x,"?"," ",str.count(x,"?"))
    if "." in x:
        x =  str.replace(x,"."," ",str.count(x,"."))
    return x