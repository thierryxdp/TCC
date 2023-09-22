def retira_pontuacao(frase):
    p = {"-":" ",",":" ", ":":" ", ";":" ",".":" ", "?":" ", "!":" ", "...":" "}
    for c in p:
        frase = str.replace(frase,c,c[p])