def retira_pontuacao(frase):
    p = {"-":" ",",":" ", ":":" ", ";":" ",".":" ", "?":" ", "!":" ", "...":" "}
    c = ["-", ",", ":", ";", ".", "?", "!", "..."]
    for c in frase:
        frase = str.replace(frase,c,p[c])
        return frase