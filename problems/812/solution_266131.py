def retira_pontuacao(frase):
    p = {"-":" ",",":" ", ":":" ", ";":" ",".":" ", "?":" ", "!":" ", "...":" "}
    for p in frase:
        frase = str.replace(frase,p,p)