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
    x= (str.split(str.lower(x)))
    list.reverse(x)
    z= " "
    return z.join(x)