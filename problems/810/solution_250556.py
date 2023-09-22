def inverte(y):
    y= str.lower(y)
    if "-" in y:
        y= str.replace(y,"-"," ",str.count(y,"-"))
    if "," in y:
        y= str.replace(y,","," ",str.count(y,","))
    if "." in y:
        y= str.replace(y,"."," ",str.count(y,"."))
    if ":" in y:
        y= str.replace(y,":"," ",str.count(y,":"))
    if "!" in y:
        y= str.replace(y,"!"," ",str.count(y,"!"))
    if "?" in y:
        y= str.replace(y,"?"," ",str.count(y,"?"))
    if ";" in y:
        y= str.replace(y,";"," ",str.count(y,";"))
    y= (str.split(y))
    list.reverse(y)
    z= ' '
    return z.join(y)