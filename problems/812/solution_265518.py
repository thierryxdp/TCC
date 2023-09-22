def retira_pontuacao (s):
    if "." in s:
        str.replace (s, ". ", " ")
    if s[(len(s)-2):] = ".":
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