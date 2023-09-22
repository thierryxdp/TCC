def conta_frases(texto):
    texto1 = (len(texto.split("...")))-1
    texto2 = (len(texto.split(".")))
    texto3 = (len(texto.split("?")))
    texto4 = (len(texto.split("!")))
    return texto1 + texto2 + texto3 + texto4