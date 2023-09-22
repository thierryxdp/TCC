def inverte(frase):
    """retorna a frase de entrada com a ordem das palavras inversa
    str->str"""
    frase= frase.replace("!"," ")
    frase= frase.replace(":"," ")
    frase= frase.replace(";"," ")
    frase= frase.replace("."," ")
    frase= frase.replace("-"," ")
    frase= frase.replace(","," ")
    frase= frase.replace("?"," ")
    frase= frase.lower()
    frase= frase.split()
    frase.reverse()
    return " " .join(frase)