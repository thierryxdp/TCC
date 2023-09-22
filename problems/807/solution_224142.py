def conta_frases(texto):
    """dado o texto, retorna a quantidade de frases presentes. Cada frase é terminada com
'.','...','!'ou'?'.
str->int"""
    texto=str.replace(texto,"!","/")
    texto=str.replace(texto,"?","/")
    texto=str.replace(texto,"...","/")
    texto=str.replace(texto,".","/")
    frases=str.split(texto,"/")
    return len(frases)-1