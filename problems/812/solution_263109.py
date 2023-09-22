def retira_pontuacao(frase):
    frase1 = str.replace(frase, ".","")
    frase2 = str.replace(frase, ",","")
    frase3 = str.replace(frase, "!","")
    frase4 = str.replace(frase, "?","")
    frase5 = str.replace(frase, "...","")
    frase6 = str.replace(frase, ";","")
    frase7 = str.replace(frase, "-","")
    return int(frase1 + frase2 + frase3 + frase4 + frase5 + frase6 + frase7)