def retira_pontuacao (s):
    if "." in s:
        s = str.replace (s, ".", " ")
    if "," in s:
        s = str.replace (s, ",", " ")
    if ":" in s:
        s = str.replace (s, ":", " ")
    if ";" in s:
        s = str.replace (s, ";", " ")
    if "-" in s:
        s = str.replace (s, "-", " ")
    if "!" in s:
        s = str.replace (s, "!", " ")
    if "?" in s:
        s = str.replace (s, "?", " ")
    return s

def inverte (s):
    y = [str.split(retira_pontuacao (s))]
    return list.reverse (y)