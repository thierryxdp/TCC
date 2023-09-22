def retira_pontuacao (p):
    if str.find (p, "-"):
        p = str. replace ("-", " ")
    if str.find (p, ","):
        p = str. replace (",", " ")
    if str.find (p, ":"):
        p = str. replace (":", " ")
    if str.find (p, ";"):
        p = str. replace (";", " ")
    if str.find (p, "."):
        p = str. replace (".", " ")
    if str.find (p, "?"):
        p = str.replace ("?", " ")
    if str.find (x, "!"):
        p = str.replace ("!", " ")
    return p