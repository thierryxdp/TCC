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
    y = (str.split(y))
    list.reverse(y)
    return str.join(y[0:1])