def inverte (y):
    if "-" in y:
        y = str.replace(y,"-"," ",str.count(y,"-"))
    if "," in y:
        y = str.replace(y,","," ",str.count(y,","))
    if ":" in y:
        y =  str.replace(y,":"," ",str.count(y,":"))
    if ";" in y:
        y =  str.replace(y,";"," ",str.count(y,";"))
    if "!" in y:
        y =  str.replace(y,"!"," ",str.count(y,"!"))
    if "?" in y:
        y =  str.replace(y,"?"," ",str.count(y,"?"))
    if "." in y:
        y =  str.replace(y,"."," ",str.count(y,"."))
    y = (list(str.split(y))
    list.reverse(y)
    return y