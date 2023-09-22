def conta_frases1(texto):
    texto = texto.replace("!","/")
    texto = texto.replace("?","/")
    texto = texto.replace("...","/")
    texto = texto.replace(".","/")
    texto = texto.split("/")
    return len(texto) - 1