def retira_pontuacao(s):
    if "-" in s:
     s = str.replace (s,"-", " ")
    if "," in s:
     s = str.replace (s, ",", " ")
    if ":" in s:
     s = str.replace (s, ":", " ")
    if ";" in s:
     s = str.replace (s, ";", " ")
    if "." in s:
     s = str.replace (s, ".", " ")
    if "?" in s:
     s = str.replace (s, "?", " ")
    if "!" in s:
     s = str.replace (s, "!", " ")
    return s