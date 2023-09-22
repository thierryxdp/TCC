def inverte(y):
    if "-" in y:
     y = str.replace (y, "-", " ", str.count(y,"-"))
    if "," in y:
     y = str.replace (y, ",", " ", str.count(y,","))
    if ":" in y:
     y = str.replace (y, ":", " ", str.count(y,":"))
    if ";" in y:
     y = str.replace (y, ";", " ", str.count(y,";"))
    if "." in y:
     y = str.replace (y, ".", " ", str.count(y,"."))
    if "!" in y:
     y = str.replace (y, "!", " ", str.count(y,"!"))
    if "?" in y:
     y = str.replace (y, "?", " ", str.count(y,"?"))
    y = (str.split(str.lower(y)))
    list.reverse(y)
     z = ' '
    return z.join(y)