def retira_pontuacao (x):
    s = ''
    if "-" in x:
        s = s + str.replace(x,"-"," ",str.count(x,"-"))
    if "," in x:
        s = s + str.replace(x,","," ",str.count(x,","))
    if ":" in x:
        s = s + str.replace(x,":"," ",str.count(x,":"))
    if ";" in x:
        s = s + str.replace(x,";"," ",str.count(x,";"))
    if "!" in x:
        s = s + str.replace(x,"!"," ",str.count(x,"!"))
    if "?" in x:
        s = s + str.replace(x,"?"," ",str.count(x,"?"))
    if "." in x:
        s = s + str.replace(x,"."," ",str.count(x,"."))
    return s