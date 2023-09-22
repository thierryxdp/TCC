def retira_pontuacao(x):
    if "-" in x:
        x= str.replace(x, "-", " ")
    elif "," in x:
        x= str.replace (x, ",", " ")
    elif ":" in x:
        x= str.replace(x, ":", " ")
    elif ";" in x:
        x= str.replace (x, ";", " ")
    elif "." in x:
        x= str.replace (x, ".", " ")
    elif "?" in x:
        x= str.replace (x, "?", " ")
    elif "!" in x:
        x= str.replace (x, "!", " ")
    return x