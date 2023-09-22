def retira_pontuacao(texto):
    "str->str"
    i=texto[:]
    if "-" in texto:
        str.replace(i,"-"," ")
    if "," in texto:
        str.replace(i,","," ")
    if ":" in texto:
        str.replace(i,":"," ")
    if ";" in texto:
        str.replace(i,";"," ")
    if "." in texto:
        str.replace(i,"."," ")
    if "!" in texto:
        str.replace(i,"!"," ")
    if "?" in texto:
        str.replace(i,"?"," ")
    return i