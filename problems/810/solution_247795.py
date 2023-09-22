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
	return txt.replace(delm, " ")

def inverte(frase):
    """
    Retorna uma (frase) com as palavras na ordem inversa,
    alem de tirar pontuacao e letras maiusculas
    str -> str
    """
    #pont_remove(frase).lower().split(" ").reverse()
    return pont_remove(frase).lower().split(" ").reverse()