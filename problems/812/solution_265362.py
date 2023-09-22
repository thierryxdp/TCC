def retira_pontuacao(texto):
    "str->str"
    if "-" in texto:
        str.replace(texto,"-"," ")
    if "," in texto:
        str.replace(texto,","," ")
    if ":" in texto:
        str.replace(texto,":"," ")
    if ";" in texto:
        str.replace(texto,";"," ")
    if "." in texto:
        str.replace(texto,"."," ")
    if "!" in texto:
        str.replace(texto,"!"," ")
    if "?" in texto:
        str.replace(texto,"?"," ")
    return texto