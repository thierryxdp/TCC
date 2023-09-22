def inverte(y):
    if "-" in y:
        y = str.replace(y, "-", " ", str.count(y, "-"))
    if "," in y:
        y = str.replace(y, ",", " ", str.count(y, ","))
    if ":" in y:
        y = str.replace(y, ":", " ", str.count(y, ":"))
    if ";" in y:
        y = str.replace(y, ";", " ", str.count(y, ";"))
    if "!" in y:
        y = str.replace(y, "!", " ", str.count(y, "!"))
    if "?" in y:
        y = str.replace(y, "?", " ", str.count(y, "?"))
    if "." in y:
        y = str.replace(y, ".", " ", str.count(y, "."))
    z = ' ' 
    return z. join (y)