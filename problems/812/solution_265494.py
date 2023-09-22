def retira_pontuacao (x):
    if "-" in x:
        s = str.replace(x,"-"," ",str.count(x,"-"))
    if "," in s:
        s= str.replace(s,","," ",str.count(s,","))
    if ":" in x:
        s =  str.replace(x,":"," ",str.count(x,":"))
    if ";" in x:
        s =  str.replace(x,";"," ",str.count(x,";"))
    if "!" in x:
        s =  str.replace(x,"!"," ",str.count(x,"!"))
    if "?" in x:
        s =  str.replace(x,"?"," ",str.count(x,"?"))
    if "." in x:
        s =  str.replace(x,"."," ",str.count(x,"."))
    return s