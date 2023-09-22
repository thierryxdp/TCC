def inverte(x):
    if "-" in x:
        x= str.replace(x,"-"," ",str.count(x,"-"))
    if "," in x:
        x= str.replace(x,","," ",str.count(x,","))
    if "." in x:
        x= str.replace(x,"."," ",str.count(x,"."))
    if ":" in x:
        x= str.replace(x,":"," ",str.count(x,":"))
    if "!" in x:
        x= str.replace(x,"!"," ",str.count(x,"!"))
    if "?" in x:
        x= str.replace(x,"?"," ",str.count(x,"?"))
    if ";" in x:
        x= str.replace(x,";"," ",str.count(x,";"))
    y= str.split(str.lower(x))
    list.reverse(y)
    z= ' '
    return z.join(x)