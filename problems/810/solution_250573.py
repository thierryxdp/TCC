def inverte (p):
    if str.find (p, "-"):
        p = str. replace (p,"-", " ")
    if str.find (p, ","):
        p = str. replace (p,",", " ")
    if str.find (p, ":"):
        p = str. replace (p,":", " ")
    if str.find (p, ";"):
        p = str. replace (p,";", " ")
    if str.find (p, "."):
        p = str. replace (p,".", " ")
    if str.find (p, "?"):
        p = str.replace (p,"?", " ")
    if str.find (p, "!"):
        p = str.replace (p,"!", " ")
    p = (str.split(str.lower(p)))
    list.reverse(p)
    x = ' '
    return x.join(p)