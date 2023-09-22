def retira_pontuacao (p):
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
    if str.find (x, "!"):
        p = str.replace (p,"!", " ")
    return p