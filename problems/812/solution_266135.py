def retira_pontuacao(frase):
    p = {"-":" ",",":" ", ":":" ", ";":" ",".":" ", "?":" ", "!":" ", "...":" "}
    c = ["-", ",", ":", ";", ".", "?", "!", "..."]
    for c in frase:
        return str.replace(frase,c,p[c])