def retira_pontuacao(texto):
    if "-" in texto:
        texto=texto.replace("-"," ")
        return texto
    if "," in texto:
        texto=texto.replace(","," ")
        return texto