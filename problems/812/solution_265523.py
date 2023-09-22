def retira_pontuacao (s):
    if "." in s:
        str.replace (s, ".", " ")
    if "," in s:
        str.replace (s, ",", " ")
    if ":" in s:
        str.replace (s, ":", " ")
    if ";" in s:
        str.replace (s, ";", " ")
    if "-" in s:
        str.replace (s, "-", " ")
    if "!" in s:
        str.replace (s, "!", " ")
    if "?" in s:
        str.replace (s, "?", " ")
    return s