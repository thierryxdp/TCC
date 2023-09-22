def pont_remove(txt):
    delm = "{}"
    txt = txt.replace("...", delm)
    txt = txt.replace(".", delm)
    txt = txt.replace("!", delm)
    txt = txt.replace("?", delm)
    txt = txt.replace(",", delm)
    txt = txt.replace(":", delm)
    txt = txt.replace(";", delm)
    txt = txt.replace("-", delm)    
	return txt.split(delm)

def inverte(frase):
    """
    Retorna uma (frase) com as palavras na ordem inversa,
    alem de tirar pontuacao e letras maiusculas
    str -> str
    """
    frase = " ".join(pont_remove(frase)).lower()
    frase = frase.split(" ")
    frase.reverse()
    return "".join(frase)