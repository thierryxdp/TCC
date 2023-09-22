def retira_pontuacao(texto):
    if "-" in texto:
        texto=str.replace(texto,"-"," ")
    if "," in texto:
        texto=str.replace(texto,","," ")
    if ":" in texto:
        texto=str.replace(texto,":"," ")
    if ";" in texto:
        texto=str.replace(texto,";"," ")
    if "." in texto:
        texto=str.replace(texto,"."," ")
    if "!" in texto:
        texto=str.replace(texto,"!"," ")
    if "?" in texto:
        texto=str.replace(texto,"?"," ")
    return texto