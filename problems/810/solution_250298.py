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
def inverte(texto):
    texto=retira_pontuacao(texto)
    texto=str.split(texto)
    texto.reverse()
    return str.join(texto," ")