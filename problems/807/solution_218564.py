def conta_frases(texto):
    texto1 = (len(texto.split("...")))-1 
    texto2 = (len(texto.split(".")))-1
    texto3 = (len(texto.split("?")))-1
    texto4 = (len(texto.split("!")))-1
    return texto1 + texto2 + texto3 + texto4