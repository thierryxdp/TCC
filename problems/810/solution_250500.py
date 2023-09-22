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
    y = (list(str.split(y)))
    if (len(y)>2):
        list.reverse(y)
    return y