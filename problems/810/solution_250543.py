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
x= str.split(x)