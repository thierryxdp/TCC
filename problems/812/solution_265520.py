def retira_pontuacao (s):
    if "." in s:
        str.replace (s, ". ", " ")
    if s[len(s)-1] = ".":
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
    if "..." in s:
        str.replace (s, "...", " ")