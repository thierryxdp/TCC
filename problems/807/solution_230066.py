def conta_frases(texto):
    "dado uma um texto com frases, retorna a quantidade destas"
    'str->int'
    i=0
    if "!" in texto:
        i=len(str.split(texto,"!"))
    if "." in texto:
        i+=len(str.split(texto,".")
    if "?" in texto:
        i+=len(str.split(texto,"?")
    if "..." in texto:
        i+=len(str.split(texto,"...")
    return i